# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from tool.util import safe_str_to_int

from questionAct import query_collect_question_list


class QueryUserConnectionQuestionListHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        grade = self.get_argument('grade', None)
        cur_page = safe_str_to_int(self.get_argument('cur_page', 1))
        page_size = safe_str_to_int(self.get_argument('page_size', 10))

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = query_collect_question_list(username, cur_page, page_size)
        self.write(result)
        self.finish()
