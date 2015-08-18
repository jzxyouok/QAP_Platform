# coding: utf8

import uuid
import time
from tool.util import SmartResponse

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
        result.update(data)
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": result,
            "msg": ""
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "data": "",
        "msg": "登录失败"
    })


def register(username, password, grade, identifier, subject, serial_number, options=None):
    """
    用户注册
    :param username: 用户名
    :param password: 密码
    :param grade: 年级
    :param identifier: 用户类别 (0: 学生 1: 教师)
    :param subject: 科目 (教师才有该选项)
    :param serial_number: 教师证 (教师才有)
    :return:
    """
    is_success = dbUser.register(username, password, grade, identifier, subject, serial_number, options)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
            "msg": "注册成功"
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "data": "",
        "msg": "注册失败"
    })


def change_password(username, old_password, new_password):
    """
    修改用户密码
    :param username: 用户名
    :param old_password: 旧密码
    :param new_password: 新密码
    :return:
    """
    is_ok, msg = dbUser.change_password(username, old_password, new_password)

    return SmartResponse().jsonwrap({
        "code": 200 if is_ok else 201,
        "data": "",
        "msg": msg
    })


def about_us(username):
    """
    关于我们
    :param username: 用户名
    :return:
    """
    is_ok, result = dbUser.about_us(username)
    return SmartResponse().jsonwrap({
        "code": 200 if is_ok else 201,
        "msg": "",
        "data": result
    })


def feedback(username, content, contact_type, contact_value):
    """
    意见反馈
    :param username: 用户名
    :param content: 反馈内容
    :param contact_type: 联系类型 (1: QQ 2: 邮箱 3: 手机)
    :param contact_value: 联系方式
    :return:
    """
    feed_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    is_ok = dbUser.feedback(username, content, contact_type, contact_value, feed_time)
    if is_ok:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
            "msg": "提交反馈成功"
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "data": "",
        "msg": "提交反馈失败"
    })
