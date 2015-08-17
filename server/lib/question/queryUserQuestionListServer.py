# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from questionAct import query_user_question_list


class QueryUserQuestionListHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        self.set_header("Content-Type", "application/json;charset=utf8")
        result = query_user_question_list(username)
        self.write(result)
        self.finish()
