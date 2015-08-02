# coding: utf8

from db.dbmanager import DBManager


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
    print 'zzz, ', data
    return data
