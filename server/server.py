# coding: utf8


"""
实现简单的http server功能
"""

import os
project_path = os.path.split(os.path.realpath(__file__))[0]
os.chdir(project_path)

import logging
import tornado.options

import tornado.ioloop
import tornado.web
import tornado.httpserver

from lib.user.loginServer import LoginHandler
from lib.user.registerServer import RegisterHandler
from lib.user.changePasswordServer import ChangePasswordHandler
from lib.user.AboutUsServer import AboutUsHandler
from lib.user.FeedbackServer import FeedBackHandler
from lib.user.SignUpServer import SignUpHandler
from lib.user.QueryUserPointsDetailServer import QueryUserPointsDetailHandler
from lib.user.FollowOtherServer import FollowOtherHandler
from lib.user.QueryFollowersServer import QueryFollowersHandler
from lib.user.ModifyPersonalInformationServer import ModifyPersonalInformationHandler
from lib.user.QueryAllInformationServer import QueryAllInformationHandler
<<<<<<< HEAD
from lib.user.resetPasswordServer import ResetUserPasswordHandler
=======
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a

from lib.email.validEmailServer import ValidEmailHandler

from lib.question.queryUserQuestionListServer import QueryUserQuestionListHandler
from lib.question.postQuestionServer import PostQuestionHandler
from lib.question.connectQuestionServer import ConnectQuestionHandler
from lib.question.searchQuestionServer import SearchQuestionHandler
from lib.question.answerQuestionServer import AnswerQuestionHandler
from lib.question.queryUserQuestionDetailServer import QueryUserQuestionDetailHandler
from lib.question.askQuestionServer import AskQuestionHandler
from lib.question.adoptAnswerServer import AdoptAnswerHandler
from lib.question.queryUserConnectionQuestionListServer import QueryUserConnectionQuestionListHandler
from lib.question.queryUserQuestionOrAnswerListServer import QueryUserQuestionOrAnswerListHandler
<<<<<<< HEAD
from lib.question.QueryAskAndAnswerPageServer import QueryAskAndAnswerPageHandler
=======
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a


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
    (r"/doUserAct/ChangePassword", ChangePasswordHandler),
    (r"/doUserAct/AboutUs", AboutUsHandler),
    (r"/doUserAct/FeedBack", FeedBackHandler),
    (r"/doUserAct/SignDaily", SignUpHandler),
    (r"/doUserAct/QueryUserPointsDetail", QueryUserPointsDetailHandler),
    (r"/doUserAct/FollowOther", FollowOtherHandler),
    (r"/doUserAct/QueryFollowers", QueryFollowersHandler),
    (r"/doUserAct/ModifyPersonalInformation", ModifyPersonalInformationHandler),
    (r"/doUserAct/QueryAllInformation", QueryAllInformationHandler),
<<<<<<< HEAD
    (r"/doUserAct/ResetUserPassword", ResetUserPasswordHandler),
=======
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
    (r"/doEmailAct/ValidEmail", ValidEmailHandler),
    (r"/doQuestionAct/QueryUserQuestionList", QueryUserQuestionListHandler),
    (r"/doQuestionAct/PostQuestion", PostQuestionHandler),
    (r"/doQuestionAct/ConnectQuestion", ConnectQuestionHandler),
    (r"/doQuestionAct/SearchQuestion", SearchQuestionHandler),
    (r"/doQuestionAct/AnswerQuestion", AnswerQuestionHandler),
    (r"/doQuestionAct/QueryUserQuestionDetail", QueryUserQuestionDetailHandler),
    (r"/doQuestionAct/AskQuestion", AskQuestionHandler),
    (r"/doQuestionAct/AdoptAnswer", AdoptAnswerHandler),
    (r"/doQuestionAct/QueryUserConnectionQuestionList", QueryUserConnectionQuestionListHandler),
<<<<<<< HEAD
    (r"/doQuestionAct/QueryUserQuestionOrAnswerList", QueryUserQuestionOrAnswerListHandler),
    (r"/doQuestionAct/QueryAskAndAnswerPage", QueryAskAndAnswerPageHandler)
=======
    (r"/doQuestionAct/QueryUserQuestionOrAnswerList", QueryUserQuestionOrAnswerListHandler)
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
])

if __name__ == '__main__':
    tornado.options.parse_command_line()
    logging.info('Starting up')
    port = 10100
    server = tornado.httpserver.HTTPServer(application)
    server.bind(port)
    server.start(1)
    tornado.ioloop.IOLoop.instance().start()
