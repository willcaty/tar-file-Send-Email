# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import datetime
import os
import time

date = str(datetime.date.today() - datetime.timedelta(days=1))

filepath = "/home/wanghao/"
suffix = '.tar.gz'
filename = date + suffix
command = "cd " + filepath + "&& tar czvf  %s %s/" % (filename, date)
os.system(command)

print "zip successfully"
time.sleep(2)

print "Start sending mail!!"
msg = MIMEMultipart()
msg["from"] = "15011273197@163.com"
to_list = ["15011273197@163.com", "13661113844@163.com"]
msg["Subject"] = "测试自动邮件"
text = MIMEText("")
msg.attach(text)

att = MIMEText(open(filepath + date + suffix, 'rb').read(), 'base62', 'gb2312')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="%s"' % (filename)
msg.attach(att)

smtp = smtplib.SMTP()
smtp.connect("smtp.163.com")
smtp.login("15011273197@163.com", 'centos121')
smtp.sendmail(msg["From"], to_list, msg.as_string())
time.sleep(2)
smtp.quit()
print 'successfully'

print "Start remove %s.tar.gz" % date
time.sleep(2)
os.remove(filepath + date + suffix)
print 'successfully'
