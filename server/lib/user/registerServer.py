# coding: utf8

"""
处理http请求
"""

import logging

import tornado.web
from tornado.httpclient import HTTPError

from userAct import register
from tool.util import safe_str_to_dict, safe_str_to_int
from conf.cm import ConfigManager


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        grade = safe_str_to_int(self.get_argument('grade'))
        identifier = safe_str_to_int(self.get_argument('identifier'))
        nickname = self.get_argument('nickname')
        subject = self.get_argument('subject', None)
        serial_number = self.get_argument('serial_number', None)
        options = self.get_argument('options', None)

        # 拿到用户头像
        files = self.request.files
        if files:
            key = 'avatar_file'
            if key in files:
                avatar_file = files[key][0]
                file_name = avatar_file['filename']
                from tool.util import get_file_extension, save_file
                suffix = get_file_extension(file_name)
                from dbop.dbUser import get_latest_id
                index = get_latest_id(username, is_new=True)
                new_file_name = "{0}_{1}{2}".format("user", index, suffix)
                msg0 = "[in registerServer] new_file_name=" + new_file_name
                logging.info(msg0)
                file_content = avatar_file['body']
                # 注入头像url字段信息
                tmp_dict = dict()
                tmp_dict['avatar_url'] = save_file(new_file_name, file_content, 1)
                tmp_dict['avatar_url'] = "http://" + ConfigManager().get_config('host') + ":" + \
                                         str(ConfigManager().get_config('port')) + tmp_dict['avatar_url']
                if options:
                    options = safe_str_to_dict(options)
                    options.update(tmp_dict)
                else:
                    options = tmp_dict.copy()
        else:
            # 注入系统默认的头像
            from tool.util import get_system_default_avatar_url
            tmp_dict = dict()
            tmp_dict['avatar_url'] = get_system_default_avatar_url()
            if options:
                options = safe_str_to_dict(options)
                options.update(tmp_dict)
            else:
                options = tmp_dict.copy()

        if subject:
            subject = safe_str_to_int(subject)
        if options:
            options = safe_str_to_dict(options)
            logging.info(options)

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = register(username, password, grade, identifier, nickname, subject, serial_number, options=options)
        self.write(result)
        self.finish()
