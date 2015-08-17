# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from questionAct import post_question


class PostQuestionHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        grade = self.get_argument('grade')
        subject = self.get_argument('subject')
        content_type = self.get_argument('content_type')
        question_content = self.get_argument('question_content')
        question_score = self.get_argument('question_score', 0)

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = post_question(username, grade, subject, content_type, question_content, question_score)
        self.write(result)
        self.finish()
