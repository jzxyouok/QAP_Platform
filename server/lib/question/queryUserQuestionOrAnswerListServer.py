# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from tool.util import safe_str_to_int

from questionAct import query_user_question_or_answer_list


class QueryUserQuestionOrAnswerListHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        identifier = safe_str_to_int(self.get_argument('identifier'))
        is_part = safe_str_to_int(self.get_argument('is_part'), 0)
        cur_page = safe_str_to_int(self.get_argument('cur_page', 1))
        page_size = safe_str_to_int(self.get_argument('page_size', 10))

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = query_user_question_or_answer_list(username, identifier, is_part, cur_page, page_size)
        self.write(result)
        self.finish()
