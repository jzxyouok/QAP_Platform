# coding: utf8

"""
负责与用户数据表交互
"""

import hashlib
from MySQLdb.cursors import DictCursor

from db.dbmanager import DBManager
from db.util import forEachPlusInsertProps, forEachUpdateProps


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
    cursor.close()
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
        cursor1.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor1.close()
        db_manager.close()
        raise Exception

    password = hashlib.sha224(password).hexdigest()
    sql0 = "insert into `%s` (%s, %s) values ('%s', '%s')" % ("tb_account", "username", "password", username, password)
    cursor0 = db_manager.conn_r.cursor()
    try:
        cursor0.execute(sql0)
        db_manager.conn_r.commit()
        cursor0.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor0.close()
        db_manager.close()
    db_manager.close()
    return True


def change_password(username, old_password, new_password):
    """
    修改密码
    :param username: 用户名
    :param old_password: 旧密码
    :param new_password: 新密码
    :return:
    """
    db_manager = DBManager()
    cursor = db_manager.conn_r.cursor(cursorclass=DictCursor)
    # 判断用户是否合法
    sql = "select password from `%s` where username='%s'" % ("tb_account", username)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    if result is None:
        return False, "用户不存在"
    tmp_password = result['password']
    password = hashlib.sha224(old_password).hexdigest()
    if tmp_password != password:
        return False, "原密码错误"
    props = dict()
    prere = dict()
    props['password'] = hashlib.sha224(new_password).hexdigest()
    prere['username'] = username
    sql0 = forEachUpdateProps("tb_account", props, prere)
    try:
        cursor0 = db_manager.conn_r.cursor()
        cursor0.execute(sql0)
        db_manager.conn_r.commit()
    except Exception:
        db_manager.conn_r.rollback()
        cursor0.close()
        db_manager.close()
        raise Exception
    db_manager.close()
    return True, "修改密码成功"


def about_us(username):
    """
    关于我们
    :param username: 用户名
    :return:
    """
    db_manager = DBManager()
    cursor = db_manager.conn_r.cursor(cursorclass=DictCursor)
    sql = "select content from `%s`" % "tb_about_us_template"
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    db_manager.close()
    if result is None:
        return False, ""
    return True, result


def feedback(username, content, contact_type, contact_value, feed_time):
    """
    意见反馈
    :param username: 用户名
    :param content: 反馈内容
    :param contact_type: 联系类型 (1: QQ 2: 邮箱 3: 手机)
    :param contact_value: 联系方式
    :param feed_time: 提交反馈的时间
    :return:
    """
    db_manager = DBManager()
    props = dict()
    props['username'] = username
    props['content'] = content
    props['contact_type'] = contact_type
    props['contact_value'] = contact_value
    props['feed_time'] = feed_time
    sql = forEachPlusInsertProps("tb_feedback", props)
    try:
        cursor = db_manager.conn_r.cursor()
        cursor.execute(sql)
        db_manager.conn_r.commit()
        cursor.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor.close()
        db_manager.close()
        raise Exception
        return False
    return True
