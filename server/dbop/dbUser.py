# coding: utf8

"""
负责与用户数据表交互
"""

from db.dbmanager import DBManager


def login(username, password):
    """
    用户登录 (学生, 教师登录入口)
    :param username: 用户名
    :param password: 密码
    :return:
    """
    db_manager = DBManager()
    sql = "select *from `%s` where username='%s' and password='%s'" % ("tb_account", username, password)
    cursor = db_manager.conn_r.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    is_ok = False
    data = None
    if result:
        cursor0 = db_manager.conn_r.cursor()
        sql0 = "select *from `%s` where username='%s'" % ("tb_user", username)
        cursor0.execute(sql0)
        result0 = cursor0.fetchone()
        is_ok = True
        data = result0
    db_manager.close()
    return is_ok, data


def register(username, password, grade, user_type, **kwargs):
    """
    用户注册 (用户获取登录账户的唯一途径)
    1. 学生注册: username, password, grade为必填项, invitation_code为选填项
    2. 教师注册: username, password, grade, subject, serial_number为必填项
    :param username: 用户名 (需要检查唯一性)
    :param password: 密码
    :param grade: 年级
    :param user_type: 用户类型 (0: 学生 1: 教师)
    :param kwargs: 可变参数 (由user_type决定)
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
    sql0 = "insert into `%s` (%s, %s) values ('%s', '%s')" % ("tb_account", "username", "password", username, password)
    cursor0 = db_manager.conn_r.cursor()
    try:
        cursor0.execute(sql0)
        db_manager.conn_r.commit()
    except Exception:
        db_manager.conn_r.rollback()
    # 键值对
    keys_tuple = []
    values_tuple = []
    keys_tuple.append("username")
    keys_tuple.append("grade")
    keys_tuple.append("identifier")
    values_tuple.append(username)
    values_tuple.append(grade)
    values_tuple.append(user_type)
    for k, v in kwargs:
        keys_tuple.append(k)
        values_tuple.append(v)
    sql1 = "insert into `%s` %s values '%s'" % ("tb_user", tuple(keys_tuple), tuple(values_tuple))
    cursor1 = db_manager.conn_r.cursor()
    try:
        cursor1.execute(sql1)
        db_manager.conn_r.commit()
    except Exception:
        db_manager.conn_r.rollback()
    db_manager.close()
    return True
