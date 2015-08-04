# coding: utf8

from db.dbmanager import DBManager
import dbop.dbUser as dbUser


def login(username, password):
    """
    用户登录
    :param username: 用户名
    :param password: 密码
    :return:
    """
    db_manager = DBManager()
    sql = "select *from `%s` where username='%s' and password='%s'" % ("tb_account", username, password)
    data = db_manager.query(sql)
    db_manager.close()
    return data


def register(username, password, grade, user_type):
    """
    用户注册
    :param username: 用户名
    :param password: 密码
    :param grade: 年级
    :param user_type: 用户类别 (0: 学生 1: 教师)
    :return:
    """
    return dbUser.register(username, password, grade, user_type)
