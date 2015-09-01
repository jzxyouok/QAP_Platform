# coding: utf8

"""
处理http请求
"""

import logging

import tornado.web
from tornado.httpclient import HTTPError

from userAct import modify_personal_information
<<<<<<< HEAD
from tool.util import safe_str_to_dict, safe_str_to_int
from conf.cm import ConfigManager
=======
from tool.util import safe_str_to_dict
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a


class ModifyPersonalInformationHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
<<<<<<< HEAD
        nickname = self.get_argument('nickname', None)
        phone_number = self.get_argument('phone_number', None)
        name = self.get_argument('name', None)
        sex = safe_str_to_dict(self.get_argument('sex', None))
        birthday = self.get_argument('birthday', None)
        address = self.get_argument('address', None)
        grade = safe_str_to_int(self.get_argument('grade', None))
        subject = safe_str_to_int(self.get_argument('subject', None))

        options = dict()
        if nickname:
            options['nickname'] = nickname
        if phone_number:
            options['phone_number'] = phone_number
        if name:
            options['name'] = name
        if sex:
            options['sex'] = sex
        if birthday:
            options['birthday'] = birthday
        if address:
            options['address'] = address
        if grade:
            options['grade'] = grade
        if subject:
            options['subject'] = subject
=======
        options = self.get_argument('props', None)
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a

        # 拿到用户头像
        props = None
        files = self.request.files
<<<<<<< HEAD
        logging.info("start!!!")
        logging.info(files)
=======
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
        if files:
            key = 'avatar_file'
            if key in files:
                avatar_file = files[key][0]
                file_name = avatar_file['filename']
                from tool.util import get_file_extension, save_file
                suffix = get_file_extension(file_name)
                from dbop.dbUser import get_latest_id
                index = get_latest_id(username)
<<<<<<< HEAD
                new_file_name = "{0}_{1}{2}".format("user", index, suffix)
=======
                new_file_name = "{0}.{1}".format(index, suffix)
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
                msg0 = "[in modifyPersonalInformationServer] new_file_name=" + new_file_name
                logging.info(msg0)
                file_content = avatar_file['body']
                # 注入头像url字段信息
                tmp_dict = dict()
                tmp_dict['avatar_url'] = save_file(new_file_name, file_content, 1)
<<<<<<< HEAD
                tmp_dict['avatar_url'] = "http://" + ConfigManager().get_config('host') + ":" + \
                                         str(ConfigManager().get_config('port')) + tmp_dict['avatar_url']
=======
>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
                if props:
                    props = safe_str_to_dict(props)
                    props.update(tmp_dict)
                else:
                    props = tmp_dict.copy()
<<<<<<< HEAD

        logging.info("yes!!!")
        logging.info(props)
=======
        if options:
            options = safe_str_to_dict(options)
            logging.info(options)

>>>>>>> 46917cd49fb2d8e06862c869e0f0c545ca7db35a
        self.set_header("Content-Type", "application/json;charset=utf8")
        result = modify_personal_information(username, props=options, options=props)
        self.write(result)
        self.finish()
