import smtplib
from email.mime.text import MIMEText
from email.header import Header


class EmailSend:
    def __init__(self):
        pass

    def qqMail(
            self, receiverMail: str,
            sendMsg: str, title: str, sendCategory: str = 'plain' or 'html',
            authorizationCode: str = '', senderMail: str = ''
    ) -> bool or str:
        """
        1、使用QQ邮箱发送邮件

        :param receiverMail: 接收者的邮箱
        :param sendMsg: 需要发送的消息
        :param title: 邮件标题
        :param sendCategory: 发送消息类型 -> plain:纯文本 or html:HTML代码
        :param authorizationCode: 发送邮箱的授权码
        :param senderMail: 发送邮箱的账号
        :return:
        """

        if sendCategory != 'plain' and sendCategory != 'html':
            return '发送消息类型不正确'
        # 构建发送内容
        msg = MIMEText(sendMsg, sendCategory, 'utf-8')
        # 发送者
        msg['From'] = Header(senderMail)
        # 接收者
        msg['To'] = Header(receiverMail)
        # 邮件标题
        msg['Subject'] = Header(title, 'utf-8')

        try:
            # 连接发信服务器
            smtpobj = smtplib.SMTP_SSL('smtp.qq.com')
            smtpobj.connect('smtp.qq.com', port=465)
            # 登录
            smtpobj.login(senderMail, authorizationCode)
            # 发送
            smtpobj.sendmail(msg=msg.as_string(), from_addr=senderMail, to_addrs=receiverMail)
            # 关闭服务器
            smtpobj.quit()
            return True
        except smtplib.SMTPException:
            return '发送失败...'


if __name__ == '__main__':
    pass
