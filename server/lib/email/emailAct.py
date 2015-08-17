# coding: utf8

import json

import dbop.dbEmail as dbEmail


def valid_email(email_address):
    """
    验证邮箱的唯一性
    :param email_address: 邮箱地址
    :return:
    """
    is_ok, msg = dbEmail.valid_email(email_address)
    return json.dumps({
        "code": 200 if is_ok else 201,
        "data": "",
        "msg": msg
    })
