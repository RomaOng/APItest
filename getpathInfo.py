# 获取当前脚本路径
import os


def get_path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path


if __name__ == '__main__':
    print('测试路径是否OK，路径为：',get_path())
