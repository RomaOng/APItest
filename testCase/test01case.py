import json
import unittest
from Common.configHttp import RunMain
import paramunittest
import geturlParams
import readExcel
import urllib.parse


url = geturlParams.geturlParams().get_url()
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login')

@paramunittest.parametrized(*login_xls)

class testUserLogin(unittest.TestCase):
    def setParameters(self,case_name,path,query,method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)


    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name+"测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        url1 = 'http://192.168.100.107:9000/User/login'
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        info = RunMain().run_main(self.method,url,data1)
        ss = json.loads(info)
        if self.case_name == 'login':
            self.assertEqual(ss['code'],200)
        if self.case_name == 'login_error':
            self.assertEqual(ss['code'],-1)
        if self.case_name == 'login_null':
            self.assertEqual(ss['code'], 10001)
