---
layout: post
title: 自动生成证书并发送给用户
---

###{{ page.title }}

最近公司网站开启全站https加证书认证，所有访问网站的用户都需要为他生成证书，并且证书有效期仅为一年，
所以需要经常给公司员工开通证书，并且需要在证书到期之前通知员工知道，所以就写了一个脚本来每天刷一遍，
将快要到期的证书重新生成。脚本还有很多不完善的地方，后续在继续修改。

~~~python
# -*- coding: utf-8 -*-

import datetime
import os
from email.Header import Header
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
import smtplib
import mimetypes
from email.MIMEAudio import MIMEAudio
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64


def get_expired_users(filename):
    """
    获取所有过期的用户
    @:param filename 需要读取的文件
    """
    today = datetime.datetime.now().strftime('%Y%m%d')
    validate_users, user_ids = [], []
    # 读取文件,获取文件内容,超时的用户记录下来,同时更新用户列表文件
    with open(filename, 'rb') as f:
        for line in f:
            line_list = line.split('\t')
            over_date = '20' + line_list[1][:6]
            username = line_list[-1].strip().split('=')[-1]
            # 还有三天就要过期的用户添加到需要生成证书的临时文件中
            if int(today)+3 > int(over_date):
                user_ids.append(username)
            else:
                validate_users.append(line)
    with open('/etc/pki/CA/tmpindexfile', 'wb') as tmp_f:
        tmp_f.writelines(validate_users)
    if os.path.exists(filename):
        bk_file = filename + '.bk'
        if os.path.exists(bk_file):
            os.remove(bk_file)
        os.rename(filename, bk_file)
    # 如果存在修改后的临时文件,则将其修改为用户证书列表文件
    if os.path.exists('/etc/pki/CA/tmpindexfile'):
        os.rename('/etc/pki/CA/tmpindexfile', filename)
    return user_ids


def auto_create_crt(filename):
    """自动创建证书"""
    user_ids = get_expired_users(filename)
    for username in user_ids:
        # 判定用户AD是否属于公司的域名
        if '@test.com' in username:
            username = username.split('@')[0]
        create_crt_for_user(username)
        auto_send_mail(username)


def create_crt_for_user(username):
    """
    为某一个用户生成证书,生成证书的同时会将该用户的信息重新写入到用户证书的信息的文件中
    :param username:
    :return:
    """
    try:
        os.system("openssl genrsa 1024 > %s.key" % username)
        os.system("openssl req -new -key %s.key -out %s.csr -subj "
                  "'/C=cn/ST=shanghai/O=***/OU=test/CN=%s/emailAddress=%s@***.com'" %
                  (username, username, username,'****'))
        os.system('openssl ca -key *** -in %s.csr -out %s.crt -batch'%(username, username))
        os.system('openssl pkcs12 -export -clcerts -in %s.crt -inkey %s.key -out %s.pfx -passout pass:' %
                  (username, username, username))
    except Exception as e:
        print "create crt error, error msg is {}".format(e)


def auto_send_mail(username):
    """
    自动为重新生成证书的用户发送邮件,此处应该开启线程来发送邮件。
　　"""
    # 创建一个带附件的实例
    msg = MIMEMultipart()
    server = smtplib.SMTP('smtp.163.com')
    server.login("username", 'password')
    try:
        # 构造附件
        crt_name = username+'.pfx'
        att = MIMEText("您好，你的证书已经过期，请在三天内下载附件中的证书，并重新安装，"
                       "否则过期后将无法登陆系统。",'base64', 'utf8')
        msg.attach(att)
        msg.attach(get_attachment("/etc/pki/tls/date/user/{}".format(crt_name)))

        msg['to'] = username+'@test.com'
        msg['Cc'] = '****@****.com'
        msg['from'] = '****@***.com'
        msg['subject'] = Header('证书 (' + str(datetime.date.today()) + ')', 'utf8')

        # 发送邮件
        server.sendmail(msg['from'], msg['to'], msg.as_string())
    except Exception as e:
        print "send mail error, error msg is {}".format(e)
        att = MIMEText("发送邮件出错！！！",'base64', 'utf8')
        msg.attach(att)
        msg['to'] = '***@****.com'
        msg['Cc'] = '****@***.com'
        msg['from'] = '****@***.com'
        msg['subject'] = Header('证书 (' + str(datetime.date.today()) + ')', 'utf8')
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

    attachment.add_header('Content-Disposition', 'attachment',   filename=os.path.basename(file_path))
    return attachment

if __name__ == '__main__':
    file_name = '/etc/pki/CA/index.txt'
    auto_create_crt(file_name)
~~~

