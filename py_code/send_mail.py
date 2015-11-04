# -*- coding: utf-8 -*-

import os
import threading
import datetime
import smtplib
import mimetypes

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.audio import MIMEAudio

from email.encoders import encode_base64


class SendMail(threading.Thread):
    """
    发送邮件的线程
    """
    def __init__(self, username):
        super(SendMail, self).__init__()
        self.username = username

    def run(self):
        # 创建一个带附件的实例
        msg = MIMEMultipart()
        server = smtplib.SMTP('smtp.163.com')
        server.login("****@163.com", '****')
        try:
            # 构造附件
            att = MIMEText("您好，你的证书已经过期，请在三天内下载附件中的证书，并重新安装，"
                           "否则过期后将无法登陆系统。",'base64', 'utf8')
            msg.attach(att)
            msg.attach(get_attachment("/home/panlei/{}".format("pgadmin.log")))

            msg['to'] = self.username+'@163.com'
            msg['from'] = '****@163.com'
            msg['subject'] = Header('证书 (' + str(datetime.date.today()) + ')', 'utf8')

            # 发送邮件
            server.sendmail(msg['from'], msg['to'], msg.as_string())
        except Exception as e:
            print "send mail error, error msg is {}".format(e)
        server.close()


def get_attachment(file_path):
    content_type, encoding = mimetypes.guess_type(file_path)

    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'

    main_type, sub_type = content_type.split('/', 1)
    with open(file_path, 'rb') as f:
        if main_type == 'text':
            attachment = MIMEText(f.read())
        elif main_type == 'image':
            attachment = MIMEImage(f.read(), _subType=sub_type)
        elif main_type == 'audio':
            attachment = MIMEAudio(f.read(), _subType=sub_type)
        else:
            attachment = MIMEBase(main_type, sub_type)
        attachment.set_payload(f.read())
        encode_base64(attachment)

    attachment.add_header(
        'Content-Disposition',
        'attachment',
        filename=os.path.basename(file_path))
    return attachment

if __name__ == "__main__":
    t = SendMail("****")
    t.start()
    t.join()
