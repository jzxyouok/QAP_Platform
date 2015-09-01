# coding: utf8

"""
处理http请求
"""

import tornado.web
from tornado.httpclient import HTTPError

from userAct import feedback


class FeedBackHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        content = self.get_argument('content')
        self.set_header("Content-Type", "application/json;charset=utf8")
        result = feedback(username, content)
        self.write(result)
        self.finish()
