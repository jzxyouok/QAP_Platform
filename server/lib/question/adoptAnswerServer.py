# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from questionAct import adopt_answer
from tool.util import safe_str_to_int


class AdoptAnswerHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        question_id = safe_str_to_int(self.get_argument('question_id'))
        answer_id = safe_str_to_int(self.get('answer_id'))
        answer_username = safe_str_to_int(self.get('answer_username'))

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = adopt_answer(username, question_id, answer_id, answer_username)
        self.write(result)
        self.finish()
