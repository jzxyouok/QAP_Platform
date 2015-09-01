# -*- coding: UTF-8 -*-

import json

from lib.email.mailbase import MailBase

f = file('conf/conf_mailnotify.json')
setting = f.read()
conf = json.loads(setting)
f.close()

MB = MailBase(conf.get("mail_host"), conf.get("mail_from"), conf.get("mail_password"))


def send_notifymail(recipient, sub, content):
    print "发送通知邮件"
    return MB.send_mail(recipient, sub, content)
