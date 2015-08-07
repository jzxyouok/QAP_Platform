# coding: utf8

import uuid
import time
import json

import dbop.dbUser as dbUser


def login(username, password):
    """
    用户登录
    :param username: 用户名
    :param password: 密码
    :return:
    """
    is_ok, data = dbUser.login(username, password)
    if is_ok:
        access_token = uuid.uuid1()
        ts = int(time.time())
        result = dict()
        result['username'] = username
        result['access_token'] = str(access_token)
        result['ts'] = ts
        return json.dumps({
            "code": 200,
            "data": result
        })
    return json.dumps({
        "code": 201,
        "data": {
            "msg": "登录失败"
        }
    })


def register(username, password, grade, user_type, options=None):
    """
    用户注册
    :param username: 用户名
    :param password: 密码
    :param grade: 年级
    :param user_type: 用户类别 (0: 学生 1: 教师)
    :return:
    """
    is_success = dbUser.register(username, password, grade, user_type, options)
    if is_success:
        return json.dumps({
            "code": 200,
            "data": {
                "msg": "注册成功"
            }
        })
    return json.dumps({
        "code": 201,
        "data": {
            "msg": "注册失败"
        }
    })
