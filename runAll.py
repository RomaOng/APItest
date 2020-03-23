import os
import Common.HTMLTestRunner as HTMLTestRunner
import getpathInfo
import unittest
import readConfig
from Common.configEmail import send_email
import pythoncom
import Common.Log
from apscheduler.schedulers.blocking import BlockingScheduler


send_email = send_email()
path = getpathInfo.get_path()
report_path = os.path.join(path, 'result')
on_off = readConfig.ReadConfig().get_email('on_off')
log = Common.Log.logger


class AllTest:
    def __init__(self):
        global resultPath
        resultPath = os.path.join(report_path, 'report.html')
        self.caseListFile = os.path.join(path, 'caselist.txt')
        self.caseFile = os.path.join(path, 'testCase')
        self.caseList = []
        log.info('resultPath'+resultPath)
        log.info('caseListFile'+self.caseListFile)
        log.info('caseList'+str(self.caseList))

    def set_case_list(self):
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n",""))
        fb.close()

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:
            case_name = case.split("/")[-1]
            print(case_name+".py")
            discover = unittest.defaultTestLoader.discover(self.caseFile,pattern=case_name+".py",top_level_dir=None)
            suite_module.append(discover)
            print('suite_module: '+str(suite_module))
        if len(suite_module)>0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            print('else: ')
            return None
        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            print("try")
            print(str(suit))
            if suit is not None:
                print('if-suit')
                fp = open(resultPath,'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report',description='Test Description')
                runner.run(suit)
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))

        finally:
            print("**********TEST END**********")
            fp.close()
        if on_off=='on':
            send_email.outlook()
        else:
            print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")


if __name__ == '__main__':
    AllTest().run()


