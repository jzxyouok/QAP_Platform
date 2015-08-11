# coding: utf8

import json

import dbop.dbQuestion as dbQuestion


def query_user_question_list(username):
    """
    查询用户的问题列表 (按照时间降序排列)
    显示结果格式说明: 用户图像, 用户名, 年级, 科目, 问题的头部, 问题的具体描述, 问题的选悬赏积分, 问题的回答数目
    :param username: 用户名
    :return:
    """
    question_list = dbQuestion.query_user_question_list(username)

    return json.dumps({
        "code": 200,
        "data": question_list
    })


def post_question(username, grade, subject, content_type, question_content, ):
    """
    用户提问
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
