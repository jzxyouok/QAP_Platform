# coding: utf8

"""
测试user相关的模块
"""

import requests

# HOST = "123.59.71.144"
HOST = "localhost"


def test_login():
    """
    测试用户登录
    :return:
    """
    params = {'username': "heavenfox@126.com", 'password': 'flyfish', "identifier": 0}
    r = requests.post("http://%s:10100/doUserAct/Login" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_register():
    """
    测试用户注册
    :return:
    """
    params = {'username': "heavenfox@126.com", 'password': 'flyfish', 'grade': 1, 'identifier': 0, 'nickname': 'cls1991', 'subject': 4,
              'serial_number': "12345678", 'options': "{'card_number': '1111111111111', 'name': u'张三', 'birthday': "
                                                      "'2015-09-11', "
                                                      "'phone_number': '000000000000', 'sex': 0, 'address': 'where'}"}
    r = requests.post("http://%s:10100/doUserAct/Register" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_AboutUs():
    """
    测试关于我们
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net"}
    r = requests.post("http://%s:10100/doUserAct/AboutUs" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_FeedBack():
    """
    测试意见反馈
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net", 'content': 'wawo'}
    r = requests.post("http://%s:10100/doUserAct/FeedBack" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_ChangePassword():
    """
    测试修改密码
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net", 'old_password': 'flyfish', 'new_password': 'flyfish'}
    r = requests.post("http://%s:10100/doUserAct/ChangePassword" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_SignUp():
    """
    测试关于我们
    :return:
    """
    params = {'username': "heavenfox@126.com"}
    r = requests.post("http://%s:10100/doUserAct/SignDaily" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_QueryUserPointsDetail():
    """
    测试关于我们
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net"}
    r = requests.post("http://%s:10100/doUserAct/QueryUserPointsDetail" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_FollowOther():
    """
    测试关于我们
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net", "other_username": "flyfish13@ifeiyu.net"}
    r = requests.post("http://%s:10100/doUserAct/FollowOther" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_QueryFollowers():
    """
    测试关于我们
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net"}
    r = requests.post("http://%s:10100/doUserAct/QueryFollowers" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_QueryUserConnectionQuestionList():
    """
    测试关于我们
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net"}
    r = requests.post("http://%s:10100/doQuestionAct/QueryUserConnectionQuestionList" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_ModifyPersonalInformation():
    """
    测试关于我们
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net", 'nickname': u'cls1991睡觉'}
    r = requests.post("http://%s:10100/doUserAct/ModifyPersonalInformation" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_QueryAllInformation():
    """
    测试关于我们
    :return:
    """
    params = {'username': "flyfish@ifeiyu.net", "identifier": 0}
    r = requests.post("http://%s:10100/doUserAct/QueryAllInformation" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


def test_ResetUserPassword():
    """
    测试重置密码
    :return:
    """
    params = {'username': "heavenfox@126.com", "email": "1553556149@qq.com"}
    r = requests.post("http://%s:10100/doUserAct/ResetUserPassword" % HOST, data=params)
    print r.cookies
    print params, '-', r.text


if __name__ == '__main__':
    # test_login()
    # test_register()
    # test_AboutUs()
    # test_FeedBack()
    # test_ChangePassword()
    # test_SignUp()
    # test_QueryUserPointsDetail()
    # test_FollowOther()
    # test_QueryFollowers()
    # test_QueryUserConnectionQuestionList()
    test_ModifyPersonalInformation()
    # test_QueryAllInformation()
    # test_ResetUserPassword()
