# coding: utf8

from tool.util import SmartResponse

import dbop.dbEmail as dbEmail


def valid_email(email_address):
    """
    验证邮箱的唯一性
    :param email_address: 邮箱地址
    :return:
    """
    is_ok, msg = dbEmail.valid_email(email_address)

    if is_ok:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
            "msg": msg
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": msg
    })
