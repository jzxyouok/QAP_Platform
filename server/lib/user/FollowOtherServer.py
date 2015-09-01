# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from userAct import follow_other


class FollowOtherHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        other_username = self.get_argument('other_username')
        self.set_header("Content-Type", "application/json;charset=utf8")
        result = follow_other(username, other_username)
        self.write(result)
        self.finish()
