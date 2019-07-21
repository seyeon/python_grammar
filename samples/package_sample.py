from samples.commonlib import func_name
from samples.commonlib import PrintUtil
from samples.commonlib import PrintUtil as Pu   # alias를 이용해서 할 수도 있다.

# Python은 File==Package, 디렉토리(__init__.py)를 포함하면 == Package로 인식 한다.
# 따라서 같은 폴더 내에 있는 파일 일지라도 함수나 클래스를 불러다 사용하려면 fullPath를 from으로 하고 import를 해야만 한다.


def url_test():
    print(func_name())
    PrintUtil.func_name()
    Pu.func_name()


if __name__ == '__main__':
    print("===========Test==========")
    url_test()
