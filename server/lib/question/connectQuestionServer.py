# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from questionAct import connect_question
from tool.util import safe_str_to_int


class ConnectQuestionHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        question_id = safe_str_to_int(self.get_argument('question_id'))

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = connect_question(username, question_id)
        self.write(result)
        self.finish()
