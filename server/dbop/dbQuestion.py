# coding: utf8

"""
负责与问题数据表交互
"""

import hashlib
from MySQLdb.cursors import DictCursor

from db.dbmanager import DBManager
from db.util import forEachPlusInsertProps


def query_user_question_list(username):
    """
    查询用户问题列表
    :param username: 用户名
    :return:
    """
    db_manager = DBManager()
    sql = "select *from `%s` where username='%s'" % ("tb_user", username)
    cursor = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    question_list = []
    if result is None or len(result) == 0:
        return question_list
    identifier = result['identifier']
    grade = result['grade']
    if identifier == 0:
        sql1 = "select *from `%s` where question_grade='%s' order by question_time desc" % ("tb_question", grade)
    elif identifier == 1:
        subject = result['subject']
        sql1 = "select *from `%s` where question_grade='%s' and question_subject = '%s' order by question_time desc" % \
               ("tb_question", username, subject)
    cursor1 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor1.execute(sql1)
    result1 = cursor1.fetchall()
    cursor1.close()
    if result1:
        for item in result1:
            tmp = item.copy()
            question_id = item['question_id']
            cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
            sql0 = "select count(*) from `%s` where question_id='%s'" % ("tb_answer", question_id)
            cursor0.execute(sql0)
            result0 = cursor0.fetchone()
            cursor0.close()
            counter = 0
            if result0:
                counter = result0[0][0]
            tmp['answer_counts'] = counter
            question_list.append(tmp)
    db_manager.close()
    return question_list


def register(username, password, grade, identifier, options=None):
    """
    用户注册 (用户获取登录账户的唯一途径)
    1. 学生注册: username, password, grade为必填项, invitation_code为选填项
    2. 教师注册: username, password, grade, subject, serial_number为必填项
    :param username: 用户名 (需要检查唯一性)
    :param password: 密码
    :param grade: 年级
    :param identifier: 用户类型 (0: 学生 1: 教师)
    :param options: 可变参数 (由user_type决定)
    :return:
    """
    db_manager = DBManager()
    cursor = db_manager.conn_r.cursor()
    # 判断用户名是否存在
    sql = "select * from `%s` where username='%s'" % ("tb_account", username)
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        db_manager.close()
        return False

    # 键值对
    prop_dict = dict()
    prop_dict['username'] = username
    prop_dict['identifier'] = identifier
    prop_dict['grade'] = grade
    if options:
        assert isinstance(options, dict)
        prop_dict.update(options)
    insert_sql = forEachPlusInsertProps('tb_user', prop_dict)
    cursor1 = db_manager.conn_r.cursor()
    try:
        cursor1.execute(insert_sql)
        db_manager.conn_r.commit()
    except Exception:
        db_manager.conn_r.rollback()
        raise Exception

    password = hashlib.sha224(password).hexdigest()
    sql0 = "insert into `%s` (%s, %s) values ('%s', '%s')" % ("tb_account", "username", "password", username, password)
    cursor0 = db_manager.conn_r.cursor()
    try:
        cursor0.execute(sql0)
        db_manager.conn_r.commit()
    except Exception:
        db_manager.conn_r.rollback()
    db_manager.close()
    return True
