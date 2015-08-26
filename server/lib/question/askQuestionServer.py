# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from questionAct import ask_question
from tool.util import safe_str_to_int


class AskQuestionHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        content_type = safe_str_to_int(self.get_argument('content_type'))
        ask_content = self.get_argument('ask_content')
        original_question_id = safe_str_to_int(self.get_argument('original_question_id'))
        be_asked_username = self.get_argument('be_asked_username')

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = ask_question(username, content_type, ask_content, original_question_id, be_asked_username)
        self.write(result)
        self.finish()
