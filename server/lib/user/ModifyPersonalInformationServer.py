# coding: utf8

"""
处理http请求
"""

import logging

import tornado.web
from tornado.httpclient import HTTPError

from userAct import modify_personal_information
from tool.util import safe_str_to_dict


class ModifyPersonalInformationHandler(tornado.web.RequestHandler):
    def get(self):
        return HTTPError(code=405)

    def post(self):
        username = self.get_argument('username')
        options = self.get_argument('props', None)

        # 拿到用户头像
        props = None
        files = self.request.files
        if files:
            key = 'avatar_file'
            if key in files:
                avatar_file = files[key][0]
                file_name = avatar_file['filename']
                from tool.util import get_file_extension, save_file
                suffix = get_file_extension(file_name)
                from dbop.dbUser import get_latest_id
                index = get_latest_id(username)
                new_file_name = "{0}.{1}".format(index, suffix)
                msg0 = "[in modifyPersonalInformationServer] new_file_name=" + new_file_name
                logging.info(msg0)
                file_content = avatar_file['body']
                # 注入头像url字段信息
                tmp_dict = dict()
                tmp_dict['avatar_url'] = save_file(new_file_name, file_content, 1)
                if props:
                    props = safe_str_to_dict(props)
                    props.update(tmp_dict)
                else:
                    props = tmp_dict.copy()
        if options:
            options = safe_str_to_dict(options)
            logging.info(options)

        self.set_header("Content-Type", "application/json;charset=utf8")
        result = modify_personal_information(username, props=options, options=props)
        self.write(result)
        self.finish()
