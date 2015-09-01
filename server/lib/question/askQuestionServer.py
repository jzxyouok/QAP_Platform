# coding: utf8

"""
处理http请求
"""

<<<<<<< HEAD
import logging

=======
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
import tornado.web
from tornado.httpclient import HTTPError

from questionAct import ask_question
from tool.util import safe_str_to_int
<<<<<<< HEAD
from conf.cm import ConfigManager
=======
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a


class AskQuestionHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
<<<<<<< HEAD
        answer_id = safe_str_to_int(self.get_argument('answer_id'))
=======
        content_type = safe_str_to_int(self.get_argument('content_type'))
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
        ask_content = self.get_argument('ask_content')
        original_question_id = safe_str_to_int(self.get_argument('original_question_id'))
        be_asked_username = self.get_argument('be_asked_username')

<<<<<<< HEAD
        options = None
        # 拿到问题相关的图片
        files = self.request.files
        if files:
            keys = ['ask_pic_file', 'ask_sound_file']
            for key in keys:
                if key in files:
                    tmp_file = files[key][0]
                    file_name = tmp_file['filename']
                    from tool.util import get_file_extension, save_file
                    suffix = get_file_extension(file_name)
                    from dbop.dbQuestion import get_latest_id
                    index = get_latest_id("tb_ask")
                    new_file_name = "{0}_{1}{2}".format("ask", index, suffix)
                    msg0 = "[in postQuestionServer] new_file_name=" + new_file_name
                    logging.info(msg0)
                    file_content = tmp_file['body']
                    # 注入url字段信息
                    tmp_dict = dict()
                    if key == 'ask_pic_file':
                        tmp_dict['ask_pic_url'] = save_file(new_file_name, file_content, 2)
                        tmp_dict['ask_pic_url'] = "http://" + ConfigManager().get_config('host') + ":" + \
                                                  str(ConfigManager().get_config('port')) + tmp_dict['ask_pic_url']
                    elif key == 'ask_sound_file':
                        tmp_dict['ask_sound_url'] = save_file(new_file_name, file_content, 3)
                        tmp_dict['ask_sound_url'] = "http://" + ConfigManager().get_config('host') + ":" + \
                                                    str(ConfigManager().get_config('port')) + tmp_dict['ask_sound_url']
                    if options is None:
                        options = tmp_dict.copy()
                    else:
                        options.update(tmp_dict)

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = ask_question(username, answer_id, ask_content, original_question_id, be_asked_username,
                              options=options)
=======
        self.set_header("Content-Type", "application/json;charset=utf8")
        result = ask_question(username, content_type, ask_content, original_question_id, be_asked_username)
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
        self.write(result)
        self.finish()
