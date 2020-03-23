import os
import win32com.client as win32
import datetime
import readConfig
import getpathInfo
from Common.Log import logger


read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')
app = str(read_conf.get_email('app'))
addressee = read_conf.get_email('addressee')
cc = read_conf.get_email('cc')
mail_path = os.path.join(getpathInfo.get_path(), 'result', 'report.html')
logger = logger

class send_email():
    def outlook(self):
        olook = win32.Dispatch("%s.Application" % app)
        # mail = olook.CreateItem(win32.constants.olMailItem)
        mail = olook.CreateItem(0)
        mail.To = addressee
        mail.CC = cc
        mail.Subject = str(datetime.datetime.now())[0:19] + '%s' % subject
        mail.Attachments.Add(mail_path, 1, 1, "myFile")
        content = """
                    执行测试中……
                    测试已完成！！
                    生成报告中……
                    报告已生成……
                    报告已邮件发送！！
        """
        mail.Body = content
        mail.Send()
        print('send email ok')
        logger.info('send email ok')


if __name__ == '__main__':
    print(subject)
    send_email().outlook()
    print("send email success")
