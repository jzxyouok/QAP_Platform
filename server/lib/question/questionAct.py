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
    is_success = dbQuestion.connect_question(username, question_id)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
            "msg": "收藏成功"
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": "已经收藏过"
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


def answer_question(username, question_id, answer_content, options=None):
    """
    回答问题
    :param username: 用户名
    :param question_id: 问题ID
    :param answer_content: 回答内容
    :return:
    """
    is_success = dbQuestion.answer_question(username, question_id, answer_content, options=options)
    if is_success:
        return SmartResponse().jsonwrap({
            "code": 200,
            "data": "",
            "msg": "回答成功"
        })
    return SmartResponse().jsonwrap({
        "code": 201,
        "msg": "没有权限回答"
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


def ask_question(username, content_type, ask_content, original_question_id, be_asked_username):
    """
    用户追问
    :param username: 用户名
    :param content_type: 追问内容类型 (1: 文字 2: 语音 3: 图片)
    :param ask_content: 追问内容
    :param original_question_id: 原问题ID
    :param be_asked_username: 被追问的用户
    :return:
    """
    is_success = dbQuestion.ask_question(username, content_type, ask_content, original_question_id, be_asked_username)
    if is_success:
        return {
            "code": 200,
            "data": "",
            "msg": "追问成功"
        }
    return {
        "code": 201,
        "msg": "追问失败"
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


