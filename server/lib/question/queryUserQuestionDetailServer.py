# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from tool.util import safe_str_to_int

from questionAct import query_user_question_detail


class QueryUserQuestionDetailHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        question_id = safe_str_to_int(self.get_argument('question_id'))

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = query_user_question_detail(username, question_id)
        self.write(result)
        self.finish()
