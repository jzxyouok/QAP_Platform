# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from userAct import reset_user_password


class ResetUserPasswordHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        email = self.get_argument('email')
        self.set_header("Content-Type", "application/json;charset=utf8")
        result = reset_user_password(username, email)
        self.write(result)
        self.finish()
