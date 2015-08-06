#coding:utf8
'''
Created on 2013-5-8

@author: lan (www.9miao.com)
'''

from gfirefly.dbentrust.dbpool import dbpool
from gfirefly.dbentrust import dbutils
from app.share import dbtransaction
from numbers import Number
from gtwisted.utils import log
import traceback


class SQLError(Exception): 
    """
    memcached key error
    """
    
    def __str__(self):
        return "memcache key error"


def forEachPlusInsertProps(tablename,props):
    assert isinstance(props, dict)
    pkeysstr = str(tuple([str(key) for key in props.keys()])).replace('\'','`')
    pvaluesstr = []
    for val in props.values():
        temp = "NULL,"
        if isinstance(val, Number):
            temp = "%s,"% val
        elif val is None:
            temp = "NULL,"
        else:
            temp = "'%s'," % val.replace("'", "\\'")
        pvaluesstr.append(temp)

    pvaluesstr = ''.join(pvaluesstr)[:-1]
    sqlstr = """INSERT INTO `%s` %s values (%s);"""%(tablename,pkeysstr,pvaluesstr)
    return sqlstr

def FormatItem(key, value):
    sqlstr = ""
    if isinstance(value, Number):
        sqlstr = " `%s`=%s " % (key, value)
    else:
        sqlstr = " `%s`='%s'  " % (key, value.replace("'", "\\'"))
    return sqlstr

def FormatCondition(props):
    """生成查询条件字符串
    """
    items = props.items()
    itemstrlist = []
    for _item in items:
        if isinstance(_item[1],Number):
            sqlstr = " `%s`=%s AND"% _item
        else:
            sqlstr = " `%s`='%s' AND "%(_item[0], _item[1].replace("'", "\\'"))
        itemstrlist.append(sqlstr)
    sqlstr = ''.join(itemstrlist)
    return sqlstr[:-4]

def FormatUpdateStr(props):
    """生成更新语句
    """
    items = props.items()
    itemstrlist = []
    for _item in items:
        if isinstance(_item[1],Number):
            sqlstr = " `%s`=%s,"% _item
        elif _item[1] is None:
            sqlstr = " `%s`= NULL ,"% (_item[0])
        else:
            sqlstr = " `%s`='%s',"% (_item[0], _item[1].replace("'", "\\'"))
        itemstrlist.append(sqlstr)
    sqlstr = ''.join(itemstrlist)
    return sqlstr[:-1]
    
def forEachUpdateProps(tablename,props,prere):
    '''遍历所要修改的属性，以生成sql语句'''
    assert isinstance(props, dict)
    pro = FormatUpdateStr(props)
    pre = FormatCondition(prere)
    sqlstr = """UPDATE `%s` SET %s WHERE %s;"""% (tablename,pro,pre)
    return sqlstr

def EachQueryProps(props):
    '''遍历字段列表生成sql语句
    '''
    sqlstr = ""
    if props == '*':
        return '*'
    elif type(props) == type([0]):
        for prop in props:
            sqlstr = sqlstr + prop +','
        sqlstr = sqlstr[:-1]
        return sqlstr
    else:
        raise Exception('props to query must be dict')
        return

def forEachQueryProps(sqlstr, props):
    '''遍历所要查询属性，以生成sql语句'''
    if props == '*':
        sqlstr += ' *'
    elif type(props) == type([0]):
        i = 0
        for prop in props:
            if(i == 0):
                sqlstr += ' ' + prop
            else:
                sqlstr += ', ' + prop
            i += 1
    else:
        raise Exception('props to query must be list')
        return
    return sqlstr

def GetTableIncrValue(tablename):
    """
    """
    conn = dbpool.connection(write=False,tablename=tablename)
    database = conn._conn._kwargs.get('db')
    sql = """SELECT AUTO_INCREMENT FROM information_schema.`TABLES` \
    WHERE TABLE_SCHEMA='%s' AND TABLE_NAME='%s';"""%(database,tablename)
    result = dbtransaction.querySql(conn, sql, is_fetch_one=True)
    if result:
        return result[0]
    return result

def ReadDataFromDB(tablename):
    """
    """
    sql = """select * from %s"""%tablename
    conn = dbpool.connection(write=False,tablename=tablename)
    result = dbtransaction.querySql(conn, sql, dictcursor=True)
    return result

def DeleteFromDB(tablename,props):
    '''从数据库中删除
    '''
    prers = FormatCondition(props)
    sql = """DELETE FROM %s WHERE %s ;"""%(tablename,prers)
    conn = dbpool.connection(write=True,tablename=tablename)
    result = dbtransaction.execSql(conn, sql)
    return result

def InsertIntoDBAndReturnID(tablename,data):
    """写入数据库,并返回ID
    """
    sql = forEachPlusInsertProps(tablename,data)
    conn = dbpool.connection(write=True,tablename=tablename)
    result, row_id = dbtransaction.execSql(conn, sql, get_row_id=True)
    return row_id

def InsertIntoDB(tablename,data):
    """写入数据库
    """
    sql = forEachPlusInsertProps(tablename,data)
    conn = dbpool.connection(write=True,tablename=tablename)
    result = dbtransaction.execSql(conn, sql)
    return result

def UpdateWithDict(tablename,props,prere):
    """更新记录
    """
    sql = forEachUpdateProps(tablename, props, prere)
    conn = dbpool.connection(write=True,tablename=tablename)
    result = dbtransaction.execSql(conn, sql)
    return result

def getAllPkByFkInDB(tablename,pkname,props):
    """根据所有的外键获取主键ID
    """
    props = FormatCondition(props)
    sql = """Select %s from `%s` where %s"""%(pkname,tablename,props)
    conn = dbpool.connection(write=False,tablename=tablename)
    result = dbtransaction.querySql(conn, sql)
    return result

def GetOneRecordInfo(tablename,props):
    '''获取单条数据的信息
    '''
    props = FormatCondition(props)
    sql = """Select * from `%s` where %s"""%(tablename,props)
    conn = dbpool.connection(write=False,tablename=tablename)
    result = dbtransaction.querySql(conn, sql, dictcursor=True, is_fetch_one=True)
    return result

def GetRecordList(tablename,pkname,pklist):
    """
    """
    pkliststr = ""
    for pkid in pklist:
        pkliststr+="%s,"%pkid
    pkliststr = "(%s)"%pkliststr[:-1]
    sql = """SELECT * FROM `%s` WHERE `%s` IN %s;"""%(tablename,pkname,pkliststr)
    conn = dbpool.connection(write=False,tablename=tablename)
    result = dbtransaction.querySql(conn, sql, dictcursor=True)
    return result

def DBTest():
    sql = """SELECT * FROM tb_item WHERE characterId=1000001;"""
    conn = dbpool.connection(write=False,tablename="tb_item")
    result = dbtransaction.querySql(conn, sql, dictcursor=True)
    return result

def getallkeys(key,redismem):
    """
    根据通配符进行keys的筛选
    :param key:  通配符
    :param redismem: redis client对象
    :return: 符合通配符的所有 主键 id
    """
    itemsinfo = redismem.keys(key)
    itemindex = []
    for items in itemsinfo:
        itemindex += [ items.split(':')[1]]
    return itemindex

def getAllPkByFkInMEM(key,fk,mem):
    pass



