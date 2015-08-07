# -*- coding: UTF-8 -*-
from MySQLdb.cursors import DictCursor

def execSql(conn, sqlstr, get_row_id=False):
    '''执行数据库的写操作(插入,修改,删除)
    @param sqlstr: str 需要执行的sql语句
    '''
    try:
        lastrowid = None
        cursor = conn.cursor()
        count = cursor.execute(sqlstr)
        conn.commit()
        if get_row_id:
            cursor.execute("SELECT LAST_INSERT_ID();")
            lastrowid = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        if count > 0:
            if get_row_id:
                return True, lastrowid
            else:
                return True
        if get_row_id:
            return False, lastrowid
        else:
            return False
    except Exception, err:
        from app.share import mylog
        mylog.err(err)
        conn.close()
        if get_row_id:
            return None, None
        else:
            return None

def execute(conn, sqlstrList):
    '''批量处理sql语句并且支持事务回滚
    @param sqlstrList: list(str) 需要执行的sql语句list
    '''
    cursor = None
    try:
        cursor = conn.cursor()
        for sqlstr in sqlstrList:
            count = cursor.execute(sqlstr)
            if count < 0:
                raise
        else:
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except Exception, err:
        from app.share import mylog
        conn.rollback()   #出现异常，事务回滚
        if cursor:
            cursor.close()
        conn.close()
        mylog.err(err)
        return False

def querySql(conn, sqlstr, dictcursor=False, is_fetch_one=False):
    '''执行数据库的查询'''
    try:
        if dictcursor:
            cursor = conn.cursor(cursorclass=DictCursor)
        else:
            cursor = conn.cursor()
        cursor.execute(sqlstr)
        if is_fetch_one:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception, err:
        from app.share import mylog
        mylog.err(err)
        conn.close()
        return None#通过放回NONE在远程调用上抛出异常

def executeInWrap(conn, execute_func):
    """
    使用函数形式进行调用事物处理
    :param conn:  连接
    :param execute_func: 执行函数，包含一个游标的接口
    :return:
    """
    cursor = None
    try:
        cursor = conn.cursor()
        result = execute_func(cursor)
        if result:
            conn.commit()
        else:
            conn.rollback()
        cursor.close()
        conn.close()
        return True
    except Exception, err:
        from app.share import mylog
        conn.rollback()   #出现异常，事务回滚
        if cursor:
            cursor.close()
        conn.close()
        mylog.err(err)
        return False