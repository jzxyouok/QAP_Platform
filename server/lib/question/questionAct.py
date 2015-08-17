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
        "data": question_list,
        "msg": ""
    })


def post_question(username, grade, subject, content_type, question_content, question_score=0):
    """
    用户提问
    :param username: 用户名
    :param grade: 年级
    :param subject: 学科
    :param content_type: 问题内容类型
    :param question_content: 问题内容
    :param question_score: 悬赏积分
    :return:
    """

    is_success = dbQuestion.post_question(username, grade, subject, content_type, question_content, question_score)
    if is_success:
        return json.dumps({
            "code": 200,
            "data": "",
            "msg": "提问成功"
        })
    return json.dumps({
        "code": 201,
        "data": "",
        "msg": "提问失败"
    })


def connect_question(username, question_id):
    """
    收藏问题
    :param username: 用户名
    :param question_id: 问题ID
    :return:
    """
    is_success = dbQuestion.connect_question(username, question_id)
    if is_success:
        return json.dumps({
            "code": 200,
            "data": "",
            "msg": "收藏成功"
        })
    return json.dumps({
        "code": 201,
        "data": "",
        "msg": "已经收藏过"
    })


def search_question(username, question_content):
    """
    搜索问题 (按照问题内容搜索)
    :param username: 用户名
    :param question_content: 问题内容
    :return:
    """
    question_list = dbQuestion.search_question(username, question_content)

    return json.dumps({
        "code": 200,
        "data": question_list,
        "msg": ""
    })


def answer_question(username, question_id, content_type, answer_content):
    """
    回答问题
    :param username: 用户名
    :param question_id: 问题ID
    :param content_type: 回答内容类型
    :param answer_content: 回答内容
    :return:
    """
    is_success = dbQuestion.answer_question(username, question_id, content_type, answer_content)
    if is_success:
        return json.dumps({
            "code": 200,
            "data": "",
            "msg": "回答成功"
        })
    return json.dumps({
        "code": 201,
        "data": "",
        "msg": "没有权限回答"
    })
