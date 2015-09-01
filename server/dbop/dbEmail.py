# coding: utf8

"""
负责与用户数据表交互
"""

from db.dbmanager import DBManager


def valid_email(email_address):
    """
    验证邮箱是否唯一
    :param email_address: 邮箱地址
    :return:
    """
    db_manager = DBManager()
    cursor_0 = db_manager.conn_r.cursor()
    # 判断邮箱地址是否存在
    sql = "select * from `%s` where username='%s'" % ("tb_account", email_address)
    cursor_0.execute(sql)
    result = cursor_0.fetchone()
    cursor_0.close()
    db_manager.close()
    if result:
        return False, "邮箱已被注册"
    return True, ""
