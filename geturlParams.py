# 读取配置文件参数并进行拼接
import readConfig as readConfig


readconfig = readConfig.ReadConfig()

class geturlParams():
    def get_url(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':8888' + '/login'
        return new_url


if __name__ == '__main__':
    print(geturlParams().get_url())
