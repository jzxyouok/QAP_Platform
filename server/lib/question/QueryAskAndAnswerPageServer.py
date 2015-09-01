# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from questionAct import query_ask_and_answer_page
from tool.util import safe_str_to_int


class QueryAskAndAnswerPageHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        answer_id = safe_str_to_int(self.get_argument('answer_id'))

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = query_ask_and_answer_page(answer_id)
        self.write(result)
        self.finish()
