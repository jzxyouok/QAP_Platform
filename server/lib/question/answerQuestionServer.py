# coding: utf8

"""
处理http请求
"""

import logging

import tornado.web
from tornado.httpclient import HTTPError

from questionAct import answer_question
from tool.util import safe_str_to_int
from conf.cm import ConfigManager


class AnswerQuestionHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        question_id = safe_str_to_int(self.get_argument('question_id'))
        answer_content = self.get_argument('answer_content')
        is_original_answer = safe_str_to_int(self.get_argument('is_original_answer', 1))

        options = None
        # 拿到问题相关的图片
        files = self.request.files
        if files:
            keys = ['answer_pic_file', 'answer_sound_file']
            for key in keys:
                if key in files:
                    tmp_file = files[key][0]
                    file_name = tmp_file['filename']
                    from tool.util import get_file_extension, save_file
                    suffix = get_file_extension(file_name)
                    from dbop.dbQuestion import get_latest_id
                    index = get_latest_id("tb_answer")
                    new_file_name = "{0}_{1}{2}".format("answer", index, suffix)
                    msg0 = "[in answerQuestionServer] new_file_name=" + new_file_name
                    logging.info(msg0)
                    file_content = tmp_file['body']
                    # 注入头像url字段信息
                    tmp_dict = dict()
                    if key == 'answer_pic_file':
                        tmp_dict['answer_pic_url'] = save_file(new_file_name, file_content, 2)
                        tmp_dict['answer_pic_url'] = "http://" + ConfigManager().get_config('host') + ":" + \
                                                     str(ConfigManager().get_config('port')) + tmp_dict['answer_pic_url']
                    elif key == 'answer_sound_file':
                        tmp_dict['answer_sound_url'] = save_file(new_file_name, file_content, 3)
                        tmp_dict['answer_sound_url'] = "http://" + ConfigManager().get_config('host') + ":" + \
                                                       str(ConfigManager().get_config('port')) + tmp_dict['answer_sound_url']
                    if options is None:
                        options = tmp_dict.copy()
                    else:
                        options.update(tmp_dict)

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = answer_question(username, question_id, answer_content, is_original_answer, options=options)
        self.write(result)
        self.finish()
