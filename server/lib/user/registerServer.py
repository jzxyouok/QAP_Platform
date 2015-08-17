# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError
import json

from userAct import register


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        grade = self.get_argument('grade')
        identifier = self.get_argument('identifier')
        subject = self.get_argument('subject', None)
        serial_number = self.get_argument('serial_number', None)
        options = self.get_argument('options', None)
        if options:
            options = json.loads(options)

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = register(username, password, grade, identifier, subject, serial_number, options=options)
        self.write(json.dumps(
            {
                "code": 200,
                "data": result
            }
        ))
        self.finish()
