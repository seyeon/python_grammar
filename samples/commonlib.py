import sys


def func_name():
    return sys._getframe(1).f_code.co_name


def caller_name():
    return sys._getframe(2).f_code.co_name


class PrintUtil:

    def __init__(self):
        self.result = 0

    @staticmethod
    def func_name():
        return sys.getframe(1).f_code.co_name

