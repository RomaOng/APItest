import requests
import json
from Common.Log import logger


logger = logger

data1 = {
    'userName': 'test_wyl',
    'userPwd': '123456',
    'token': ''
}


class RunMain():

    def send_post(self, url, data):

        result = requests.post(url=url, data=data, allow_redirects=False)
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        res = result.headers['Set-Cookie']
        return res

    def send_get(self, url, cookie=None):
        header = {
            "Cookie": cookie
        }
        result = requests.get(url=url, headers=header)
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        res = result.status_code
        return res

    def run_main(self, method, url=None, data=None, cookie=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data)
            logger.info(str(result))

        elif method == 'get':
            result = self.send_get(url, cookie)
            logger.info(str(result))
        else:
            print("method错误")
            logger.info("method 错误!")
        return result


# 通过写死参数，来验证我们写的请求是否正确
if __name__ == "__main__":
    result1 = RunMain().run_main('post', "http://192.168.100.107:9000/User/Login", data1)
    print(result1)

    result2 = RunMain().run_main('get', "http://192.168.100.107:9000/new/newIndex", data=None, cookie=result1)
    print(result2)
