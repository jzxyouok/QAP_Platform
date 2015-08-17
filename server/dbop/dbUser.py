# coding: utf8

"""
负责与用户数据表交互
"""

import hashlib
from MySQLdb.cursors import DictCursor

from db.dbmanager import DBManager
from db.util import forEachPlusInsertProps


def login(username, password):
    """
    用户登录 (学生, 教师登录入口)
    :param username: 用户名
    :param password: 密码
    :return:
    """
    password = hashlib.sha224(password).hexdigest()
    db_manager = DBManager()
    sql = "select *from `%s` where username='%s' and password='%s'" % ("tb_account", username, password)
    cursor = db_manager.conn_r.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    is_ok = False
    data = None
    if result:
        cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        sql0 = "select *from `%s` where username='%s'" % ("tb_user", username)
        cursor0.execute(sql0)
        result0 = cursor0.fetchone()
        is_ok = True
        data = result0
    db_manager.close()
    return is_ok, data


def register(username, password, grade, identifier, subject, serial_number, options=None):
    """
    用户注册 (用户获取登录账户的唯一途径)
    1. 学生注册: username, password, grade为必填项, invitation_code为选填项
    2. 教师注册: username, password, grade, subject, serial_number为必填项
    :param username: 用户名 (需要检查唯一性)
    :param password: 密码
    :param grade: 年级
    :param identifier: 用户类型 (0: 学生 1: 教师)
    :param subject: 科目 (教师才有该选项)
    :param serial_number: 教师证 (教师才有)
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
    if subject is not None:
        prop_dict['subject'] = subject
    if serial_number is not None:
        prop_dict['serial_number'] = serial_number
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
