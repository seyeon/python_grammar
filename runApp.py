from samples import class_n_general
from samples.class_n_general import Rectangle
from samples.thread_process import *

#계산기 클래스
class FourCal:
    age = 0
    nick = 'hyomin'

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setData(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.second

    def div(self):
        return self.first / self.second

    def list(self):
        return [self.first, self.second]

    @staticmethod
    def nick_name():
        return 'seyeon_name'

    @staticmethod
    def config():
        return {1: 'abcd', 2: 'bdedf'}

    @staticmethod
    def array_func(*args):
        print(args)

        for var in args:
            print(var)

    def print_nickname(self):
        print('print_nickname')
        print(self.nick)

    @staticmethod
    def result_tuple(a, b):
        return a + b, a * b

    @classmethod
    def print_class_nickname(cls):
        print('print_class_nickname')
        print(FourCal.nick)


class MoreCal(FourCal):
    pass


class TestClass:
    age = 10
    name = 'syeeon'

    def print_instance_information(self):
        print("print_instance_information")
        print("age = {}, name= {}".format(self.age, self.name))

    @classmethod
    def print_class_information(cls):
        print("print_class_information")
        print("age = {}, name= {}".format(cls.age, cls.name))

    @staticmethod
    def print_class_variable():
        print('age = {}, name = {}'.format(TestClass.age, TestClass.name))


def test_coroutine(i):
    print('start test1 coroutine')
    while True:
        yield i
        i += 1
        print("coroutine value = " + str(i))


def calc(*numbers):
    count = 0
    tot = 0
    for n in numbers:
        count += 1
        tot += n
    return count, tot

result = 0
zeroValue = 0

FUL_NAME = "swift"

if __name__ == '__main__':
    # cal = FourCal(10, 20)
    # moreCla = MoreCal
    # moreCalInstance = MoreCal()

    # result = calc(1, 2, 3, 4)
    # print(result)
    # print(str(result[0]) + str(":") + str(result[1]))


    # rectangle = Rectangle(10, 30)
    # rectangle.__on_draw()

    # rect.__clear_rect(rectangle)
    # class_n_general.clear_rect(rectangle)

    FUL_NAME = "Thread begin"
    run_thread()

    FUL_NAME = "Thread end"

    # co = test_coroutine(1)
    # co.send(1)
    # co.send(2)

