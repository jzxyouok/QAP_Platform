# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from questionAct import search_question


class SearchQuestionHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        question_content = self.get_argument('question_content')

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = search_question(username, question_content)
        self.write(result)
        self.finish()
