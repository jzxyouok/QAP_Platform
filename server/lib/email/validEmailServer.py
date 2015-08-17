# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from emailAct import valid_email


class ValidEmailHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        email_address = self.get_argument('email_address')

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = valid_email(email_address)
        self.write(result)
        self.finish()
