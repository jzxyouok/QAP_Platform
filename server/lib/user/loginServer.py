# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from tool.util import safe_str_to_int
from userAct import login


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        identifier = safe_str_to_int(self.get_argument('identifier'))
        self.set_header("Content-Type", "application/json;charset=utf8")
        result = login(username, password, identifier)
        self.write(result)
        self.finish()
