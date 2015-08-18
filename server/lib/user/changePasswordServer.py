# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from userAct import change_password


class ChangePasswordHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        old_password = self.get_argument('old_password')
        new_password = self.get_argument('new_password')
        self.set_header("Content-Type", "application/json;charset=utf8")
        result = change_password(username, old_password, new_password)
        self.write(result)
        self.finish()
