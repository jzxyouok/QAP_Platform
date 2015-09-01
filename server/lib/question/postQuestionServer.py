# coding: utf8

"""
处理http请求
"""

import logging

import tornado.web
from tornado.httpclient import HTTPError

from questionAct import post_question
from tool.util import safe_str_to_int
<<<<<<< HEAD
from conf.cm import ConfigManager
=======
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a


class PostQuestionHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        grade = safe_str_to_int(self.get_argument('grade'))
        subject = safe_str_to_int(self.get_argument('subject'))
<<<<<<< HEAD
        question_content = self.get_argument('question_content', None)
=======
        question_content = self.get_argument('question_content')
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
        question_score = safe_str_to_int(self.get_argument('question_score', 0))

        options = None
        # 拿到问题相关的图片
        files = self.request.files
        if files:
            keys = ['question_pic_file', 'question_sound_file']
            for key in keys:
                if key in files:
                    tmp_file = files[key][0]
                    file_name = tmp_file['filename']
                    from tool.util import get_file_extension, save_file
                    suffix = get_file_extension(file_name)
                    from dbop.dbQuestion import get_latest_id
<<<<<<< HEAD
                    index = get_latest_id("tb_question")
                    new_file_name = "{0}_{1}{2}".format("question", index, suffix)
=======
                    index = get_latest_id(username, "tb_question", "question_id")
                    new_file_name = "{0}_{1}.{2}".format("question", index, suffix)
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
                    msg0 = "[in postQuestionServer] new_file_name=" + new_file_name
                    logging.info(msg0)
                    file_content = tmp_file['body']
                    # 注入头像url字段信息
                    tmp_dict = dict()
                    if key == 'question_pic_file':
                        tmp_dict['question_pic_url'] = save_file(new_file_name, file_content, 2)
<<<<<<< HEAD
                        tmp_dict['question_pic_url'] = "http://" + ConfigManager().get_config('host') + ":" + \
                                                       str(ConfigManager().get_config('port')) + tmp_dict['question_pic_url']
                    elif key == 'question_sound_file':
                        tmp_dict['question_sound_url'] = save_file(new_file_name, file_content, 3)
                        tmp_dict['question_sound_url'] = "http://" + ConfigManager().get_config('host') + ":" + \
                                                         str(ConfigManager().get_config('port')) + tmp_dict['question_sound_url']
                    if options is None:
                        options = tmp_dict.copy()
                    else:
                        options.update(tmp_dict)
=======
                    elif key == 'question_sound_file':
                        tmp_dict['question_sound_url'] = save_file(new_file_name, file_content, 3)
                    options = tmp_dict.copy()
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = post_question(username, grade, subject, question_content, question_score, options=options)
        self.write(result)
        self.finish()
