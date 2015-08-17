# coding: utf8


"""
实现简单的http server功能
"""

import os
project_path = os.path.split(os.path.realpath(__file__))[0]
os.chdir(project_path)

import tornado.ioloop
import tornado.web
import tornado.httpserver

from lib.user.loginServer import LoginHandler
from lib.user.registerServer import RegisterHandler

from lib.email.validEmailServer import ValidEmailHandler

from lib.question.queryUserQuestionListServer import QueryUserQuestionListHandler
from lib.question.postQuestionServer import PostQuestionHandler
from lib.question.connectQuestionServer import ConnectQuestionHandler
from lib.question.searchQuestionServer import SearchQuestionHandler
from lib.question.answerQuestionServer import AnswerQuestionHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        """
        处理get请求
        :return:
        """
        self.write('handle get')
        self.finish()

    def post(self, *args, **kwargs):
        """
        处理post请求
        :param args:
        :param kwargs:
        :return:
        """
        self.write('handle post')
        self.finish()

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/doUserAct/Login", LoginHandler),
    (r"/doUserAct/Register", RegisterHandler),
    (r"/doEmailAct/ValidEmail", ValidEmailHandler),
    (r"/doQuestionAct/QueryUserQuestionList", QueryUserQuestionListHandler),
    (r"/doQuestionAct/PostQuestion", PostQuestionHandler),
    (r"/doQuestionAct/ConnectQuestion", ConnectQuestionHandler),
    (r"/doQuestionAct/SearchQuestion", SearchQuestionHandler),
    (r"/doQuestionAct/AnswerQuestion", AnswerQuestionHandler)
])

if __name__ == '__main__':
    port = 10100
    server = tornado.httpserver.HTTPServer(application)
    server.bind(port)
    server.start(1)
    tornado.ioloop.IOLoop.instance().start()
