# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError
import json

from questionAct import answer_question


class AnswerQuestionHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        question_id = self.get_argument('question_id')
        content_type = self.get_argument('content_type')
        answer_content = self.get_argument('answer_content')

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = answer_question(username, question_id, content_type, answer_content)
        self.write(json.dumps(
            {
                "code": 200,
                "data": result
            }
        ))
        self.finish()
