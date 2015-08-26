# coding: utf8

"""
测试question相关的模块
"""

# HOST = "123.59.71.144"
HOST = "localhost"

import requests


def test_QueryUserQuestionList():
    """
    测试请求问题列表
    :return:
    """
    params = {'username': "caiyuanpei@vip.qq.com"}
    r = requests.post("http://%s:10100/doQuestionAct/QueryUserQuestionList" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_PostQuestion():
    """
    测试用户提问
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net", 'grade': 1, 'subject': 4, 'content_type': 1, 'question_content':
              'hello', 'question_score': 20}
    r = requests.post("http://%s:10100/doQuestionAct/PostQuestion" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_ConnectQuestion():
    """
    测试收藏问题
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net", 'question_id': 3}
    r = requests.post("http://%s:10100/doQuestionAct/ConnectQuestion" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_SearchQuestion():
    """
    测试用户搜索问题
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net", 'question_content': 'hel', "page_size": 2}
    r = requests.post("http://%s:10100/doQuestionAct/SearchQuestion" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_AnswerQuestion():
    """
    测试回答问题
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net", 'question_id': 3, 'content_type': 1, 'answer_content': 'wawo'}
    r = requests.post("http://%s:10100/doQuestionAct/AnswerQuestion" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_QueryUserQuestionDetail():
    """
    测试回答问题
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net", 'question_id': 3}
    r = requests.post("http://%s:10100/doQuestionAct/QueryUserQuestionDetail" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_QueryUserConnectionQuestionList():
    """
    测试用户搜索问题
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net", "page_size": 2}
    r = requests.post("http://%s:10100/doQuestionAct/QueryUserConnectionQuestionList" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


if __name__ == '__main__':
    test_QueryUserQuestionList()
    test_AnswerQuestion()
    test_PostQuestion()
    test_ConnectQuestion()
    test_AnswerQuestion()
    test_SearchQuestion()
    test_QueryUserQuestionDetail()
    test_QueryUserConnectionQuestionList()
