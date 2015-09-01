# coding: utf8

"""
测试question相关的模块
"""

# HOST = "123.59.71.144"
HOST = "localhost"
# HOST = "61.158.108.30"

import requests


def test_QueryUserQuestionList():
    """
    测试请求问题列表
    :return:
    """
    params = {'username': "heavenfox@126.com"}
    r = requests.post("http://%s:10100/doQuestionAct/QueryUserQuestionList" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_PostQuestion():
    """
    测试用户提问
    :return:
    """
    params = {'username': "heavenfox@126.com", 'grade': 1, 'subject': 4, 'question_content':
              'hello', 'question_score': 3}
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
    params = {'username': "flyfish@ifeiyu.net", 'question_id': 8, 'answer_content': 'wawo'}
    r = requests.post("http://%s:10100/doQuestionAct/AnswerQuestion" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_QueryUserQuestionDetail():
    """
    测试回答问题
    :return:
    """
    params = {'username': "liangcheng@hrbmu.edu.cn", 'question_id': 16}
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


def test_AskQuestion():
    """
    测试用户追问
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net", 'ask_content':
              'hello', 'be_asked_username': "caiyuanpei4@vip.qq.com", "original_question_id": 99, "answer_id": 5}
    r = requests.post("http://%s:10100/doQuestionAct/AskQuestion" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_QueryAskAndAnswerPage():
    """
    测试用户追问
    :return:
    """
    params = {'answer_id': 48}
    r = requests.post("http://%s:10100/doQuestionAct/QueryAskAndAnswerPage" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_AdoptAnswer():
    """
    测试采纳回答
    :return:
    """
    params = {'username': "heavenfox@126.com", 'question_id':
              8, 'answer_id': 2, "answer_username": "flyfish@ifeiyu.net"}
    r = requests.post("http://%s:10100/doQuestionAct/AdoptAnswer" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


if __name__ == '__main__':
    test_QueryUserQuestionList()
    # test_AnswerQuestion()
    # test_PostQuestion()
    # test_ConnectQuestion()
    # test_AnswerQuestion()
    # test_SearchQuestion()
    # test_QueryUserQuestionDetail()
    # test_QueryUserConnectionQuestionList()
    # test_AskQuestion()
    # test_QueryAskAndAnswerPage()
    # test_AdoptAnswer()
