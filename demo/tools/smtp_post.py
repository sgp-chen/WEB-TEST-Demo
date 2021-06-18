import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import glob, os

class email_():
    def file_path(self):
        tmp_path = os.path.join("../", "report")
        ##查找tmp-开头的文件路径名
        tmp_dirs = glob.glob(os.path.join(tmp_path, '测试报告*.html'))
        ## 获取路径中的文件名
        ## 可通过os.path.split分割，可避免windows和linux的分隔符不同的问题
        file_name = os.path.split(tmp_dirs[-1])[-1]
        return file_name

    def mail_(self):
        mail_host = "smtp.qq.com"
        mail_user = "623374926@qq.com"
        mail_pass = "gfibgbvsyvctbahj"
        sender = '623374926@qq.com'
        receivers = ['623374926@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = Header("测试", 'utf-8')
        subject = 'Python 自动化测试报告'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('自动化测试报告，请见附件', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        file = open("../report/" + email_().file_path(), 'r+', encoding="utf-8").read()
        att1 = MIMEText(str(file), 'html', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1.add_header("Content-Disposition", "attachment", filename=("utf-8", "", "测试报告.html"))
        message.attach(att1)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 587)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


if __name__ == '__main__':
    email_().mail_()
