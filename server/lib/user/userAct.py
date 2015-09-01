# coding: utf8

import uuid
import time
from tool.util import SmartResponse

import dbop.dbUser as dbUser


def login(username, password, identifier):
    """
    用户登录
    :param username: 用户名
    :param password: 密码
    :return:
    """
    is_ok, data = dbUser.login(username, password, identifier)
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
        "msg": "登录失败"
    })


def register(username, password, grade, identifier, nickname, subject, serial_number, options=None):
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
    is_success = dbUser.register(username, password, grade, identifier, nickname, subject, serial_number, options=options)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
            "msg": "注册成功"
        })
    return SmartResponse().jsonwrap({
        "code": 201,
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


def about_us(username):
    """
    关于我们
    :param username: 用户名
    :return:
    """
    is_ok, result = dbUser.about_us(username)

    if is_ok:
        return SmartResponse().jsonwrap({
            "code": 200,
            "msg": "",
            "data": result
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": "查看失败"
    })


def feedback(username, content):
    """
    意见反馈
    :param username: 用户名
    :param content: 反馈内容
    :return:
    """
    feed_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    is_ok = dbUser.feedback(username, content, feed_time)
    if is_ok:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
            "msg": "提交反馈成功"
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": "提交反馈失败"
    })


def sign_up(username):
    """
    每日签到
    :param username: 用户名
    :return:
    """
    sign_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    is_ok, msg, data = dbUser.sign_up(username, sign_time)
    if is_ok:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": {
                "score_point_add": data
            },
            "msg": msg
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": msg
    })


def query_user_points_detail(username):
    """
    请求用户积分详情
    :param username: 用户名
    :return:
    """
    is_ok, data = dbUser.query_user_points_detail(username)
    if is_ok:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": data,
            "msg": ""
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": "请求用户积分详情失败"
    })


def follow_other(username, other_username):
    """
    关注其他用户
    :param username: 用户名
    :param other_username: 其他的用户名
    :return:
    """
    is_ok = dbUser.follow_other(username, other_username)
    if is_ok:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
            "msg": "关注成功"
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": "已经关注过"
    })


def query_followers(username):
    """
    请求关注/粉丝数量
    :param username: 用户名
    :return:
    """
    is_ok, follows_num, fans_num = dbUser.query_followers(username)
    if is_ok:
        result = {
            "follows_num": int(follows_num),
            "fans_num": int(fans_num)
        }
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": result,
            "msg": ""
        })
    return {
        "code": 201,
        "msg": "请求关注/粉丝失败"
    }


def query_collection_question_list(username):
    """
    请求用户收藏的问题列表
    :param username: 用户名
    :return:
    """
    is_ok, result = dbUser.query_collection_question_list(username)
    if is_ok:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": result,
            "msg": ""
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": "请求收藏问题列表失败"
    })


def modify_personal_information(username, props=None, options=None):
    """
    更新个人信息
    :param username: 用户名
    :param props: 更新的数据域
    :param options: 头像信息字段
    :return:
    """
<<<<<<< HEAD
    is_ok, result = dbUser.modify_personal_information(username, props=props, options=options)
    if is_ok:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": result if result else "",
=======
    is_ok = dbUser.modify_personal_information(username, props=props, options=options)
    if is_ok:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
            "msg": "修改成功"
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": "修改失败"
    })


def query_all_information(username, identifier):
    """
    请求我的页面数据
    :param username: 用户名
    :param identifier: 身份标志
    :return:
    """
    is_ok, data = dbUser.query_all_information(username, identifier)
    if is_ok:
        return {
            "code": 200,
            "data": data,
            "msg": ""
        }

<<<<<<< HEAD

def reset_user_password(username, email):
    """
    忘记密码
    :param username: 用户名
    :param email: 邮箱地址
    :return:
    """
    is_ok, data = dbUser.reset_user_password(username, email)
    if is_ok:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": data,
            "msg": ""
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": data
    })

=======
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
