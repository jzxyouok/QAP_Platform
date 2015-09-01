# coding: utf8

from tool.util import SmartResponse

import dbop.dbQuestion as dbQuestion


def query_user_question_list(username, cur_page, page_size):
    """
    查询用户的问题列表 (按照时间降序排列)
    显示结果格式说明: 用户图像, 用户名, 年级, 科目, 问题的头部, 问题的具体描述, 问题的选悬赏积分, 问题的回答数目
    :param username: 用户名
    :return:
    """
    is_success, question_list, counts = dbQuestion.query_user_question_list(username, cur_page, page_size)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": {
                "cur_page": cur_page,
                "page_size": page_size,
                "counts": counts,
                "question_list": question_list
            },
            "msg": ""
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": "数据请求失败"
    })


def post_question(username, grade, subject, question_content, question_score=0, options=None):
    """
    用户提问
    :param username: 用户名
    :param grade: 年级
    :param subject: 学科
    :param question_content: 问题内容
    :param question_score: 悬赏积分
    :param options: 可变字段
    :return:
    """

    is_success = dbQuestion.post_question(username, grade, subject, question_content, question_score,
                                          options=options)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
            "msg": "提问成功"
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": "提问失败"
    })


def connect_question(username, question_id):
    """
    收藏问题
    :param username: 用户名
    :param question_id: 问题ID
    :return:
    """
    is_success, msg = dbQuestion.connect_question(username, question_id)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
            "msg": "收藏成功"
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": msg
    })


def query_collect_question_list(username, cur_page, page_size):
    """
    请求用户收藏的问题列表
    :param username: 用户名
    :param cur_page: 当前数据分页
    :param page_size: 每页显示数据条数
    :return:
    """
    is_success, question_list, counts = dbQuestion.query_collect_question_list(username, cur_page, page_size)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": {
                "question_list": question_list,
                "cur_page": cur_page,
                "page_size": page_size,
                "counts": counts
            },
            "msg": ""
        })


def search_question(username, question_content, cur_page, page_size, grade=None, subject=None):
    """
    搜索问题 (按照问题内容搜索)
    :param username: 用户名
    :param question_content: 问题内容
    :param grade: 年级 (默认值: None)
    :param subject: 科目 (默认值: None)
    :return:
    """
    is_success, question_list, counts = dbQuestion.search_question(username, question_content, cur_page, page_size, grade, subject)

    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": {
                "cur_page": cur_page,
                "page_size": page_size,
                "question_list": question_list,
                "counts": counts
            },
            "msg": ""
        })


def answer_question(username, question_id, answer_content, is_original_answer, options=None):
    """
    回答问题
    :param username: 用户名
    :param question_id: 问题ID
    :param answer_content: 回答内容
    :param is_original_answer: 是否是原回答(1: 原回答 0: 追答)
    :return:
    """
    is_success, msg = dbQuestion.answer_question(username, question_id, answer_content, is_original_answer,
                                                 options=options)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
            "msg": "回答成功"
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": msg
    })


def query_user_question_detail(username, question_id):
    """
    请求用户问题详情
    :param username: 用户名
    :param question_id: 问题ID
    :return:
    """
    is_success, data = dbQuestion.query_user_question_detail(username, question_id)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": data,
            "msg": ""
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": "没有该问题"
    })


def ask_question(username, answer_id, ask_content, original_question_id, be_asked_username, options):
    """
    用户追问
    :param username: 用户名
    :param answer_id: 回答的ID
    :param ask_content: 追问内容
    :param original_question_id: 原问题ID
    :param be_asked_username: 被追问的用户
    :return:
    """
    is_success, msg = dbQuestion.ask_question(username, answer_id, ask_content, original_question_id, be_asked_username,
                                              options)
    if is_success:
        return {
            "code": 200,
            "data": "",
            "msg": "追问成功"
        }
    return {
        "code": 201,
        "msg": msg
    }


def adopt_answer(username, question_id, answer_id, answer_username):
    """
    采纳回答
    :param username: 用户名
    :param question_id: 原问题ID
    :param answer_id: 回答的ID
    :param answer_username: 回答者的用户名
    :return:
    """
    is_success, msg = dbQuestion.adopt_answer(username, question_id, answer_id, answer_username)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
            "msg": "采纳成功"
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": msg
    })


def query_user_question_or_answer_list(username, identifier, is_part, cur_page, page_size):
    """
    请求用户的问题列表或者回答列表
    :param username: 用户名
    :param identifier: 身份标志 (0: 学生 1: 教师)
    :param is_part: 按照条件搜索 (学生: 问题完成数 教师： 回答采纳数)
    :param cur_page: 当前数据分页
    :param page_size: 每页显示数据条数
    :return:
    """
    is_success, question_list, counts = dbQuestion.query_user_question_or_answer_list(username, identifier, is_part,
                                                                                      cur_page, page_size)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": {
                "question_list": question_list,
                "page_size": page_size,
                "cur_page": cur_page,
                "counts": counts
            },
            "msg": ""
        })


def query_ask_and_answer_page(answer_id):
    """
    请求用户问题的追问追答列表
    :param answer_id: 回答的ID
    :return:
    """
    is_success, data = dbQuestion.query_ask_and_answer_page(answer_id)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": data,
            "msg": ""
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": data
    })
