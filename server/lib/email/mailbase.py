# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText


class MailBase():
    def __init__(self, mail_host=None, mail_from=None, mail_password=None):
        self.mail_from = mail_from
        self.mail_password = mail_password
        self.mail_host = mail_host

    # to_list：收件人；sub：主题；content：邮件内容
    def send_mail(self, to_list, subject, content):
        msg = MIMEText(content, _subtype='html', _charset='utf8')  #创建一个实例，这里设置为html格式邮件
        msg['Subject'] = subject  #设置主题
        msg['From'] = self.mail_from
        msg['To'] = ";".join(to_list)
        try:
            s = smtplib.SMTP()
            s.connect(self.mail_host)  #连接smtp服务器
            s.login(self.mail_from, self.mail_password)  #登陆服务器
            s.sendmail(self.mail_from, to_list, msg.as_string())  #发送邮件
            s.quit()
            return True
        except Exception, e:
            print str(e)
            return False
        pass