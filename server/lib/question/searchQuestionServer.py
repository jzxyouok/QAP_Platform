# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from tool.util import safe_str_to_int

from questionAct import search_question


class SearchQuestionHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        grade = self.get_argument('grade', None)
        subject = self.get_argument('subject', None)
        cur_page = safe_str_to_int(self.get_argument('cur_page', 1))
        page_size = safe_str_to_int(self.get_argument('page_size', 10))
        question_content = self.get_argument('question_content')

        if grade is not None:
            grade = safe_str_to_int(grade)
        if subject is not None:
            subject = safe_str_to_int(subject)

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = search_question(username, question_content, cur_page, page_size, grade=grade, subject=subject)
        self.write(result)
        self.finish()
