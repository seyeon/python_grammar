import os

from urllib.request import urlopen
from samples.commonlib import func_name
from samples.commonlib import PrintUtil


def url_test():
    print(func_name())
    f = urlopen("http://www.example.com")
    print(f.read(500).decode('utf-8'))

    PrintUtil.func_name()


if __name__ == '__main__':
    print("===========Test==========")
    url_test()




