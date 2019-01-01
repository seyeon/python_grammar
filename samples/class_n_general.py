import os

import enum
from abc import *  # 추상클래스를 사용하려면 필요함
# from math import factorial as fac  # alias사용할 수 있음


# 파이썬은 파일, 클래스를 모두 모듈로 본다.
# from 모듈명(파일명) import * (클래스명, 메소드명)


# enum 값 정의
class Color(enum.Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    BLUE_LIGHT = 2  # 같은 값의 선언이 됨
    BLACK = enum.auto()  # 1부터 시작해서 1씩 증가


# 추상 클래스
class Model(metaclass=ABCMeta):

    def __init__(self):
        print("Model __init__")

    # @abc를 사용할 수도 있음, 상속받은 곳에서는 반드시 Override해야 함, from abc import *
    # 단 __ = private, _ = protected 임을 주의해야 한다.
    @abstractmethod
    def _on_draw(self):
        pass


# 클래스 카멜 케이스
class Rectangle(Model):
    count = 0  # 클래스 변수, 언더스코 명명 방식 대문자 금지, _로 단어 분리
    _name = 'Jack\'s rect'  # protected 클래스 변수

    OBJECT_NAME = 'object'

    # 생성자
    def __init__(self, width, height):
        super().__init__()      # 상위 클래스의 생성자 호출

        self.width = width      # public property 맴버변수
        self.height = height
        self.__color = Color.BLUE  # private instance 맴버 변
        print('setting color is {}'.format(self.__color.name))
        Rectangle.count += 1

    # 소멸자
    def __del__(self):
        pass

    # 연산자 오버로딩 +, __sub__, __cmp__,
    def __add__(self, other):
        obj = Rectangle(self.width + other.width, self.height + other.height)
        return obj

    # _ = instance.color 가능함
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, clr):
        self.__color = clr

    # public 인스턴스 메서드, 언더스코프 명명 방식 대문자 금지, _로 단어 분리
    def calc_area(self):    # 반드시 self를 포함 해야함
        area = self.width * self.height  # area는 로컬 변수임
        return area

    # 추상클래스에서 Override된 protected 인스턴스 메서드, 시작을 _로 함.
    def _on_draw(self):
        print('height = {}, width = {}'.format(self.height, self.width))
        print('called on_draw')

    # private메소드 __로 시작함
    def __on_calc(self):
        pass

    # 정적 메서드 utillity등을 만들때 사용
    @staticmethod
    def is_square(width, height):
        return width == height

    @staticmethod
    def is_big_square(rect):
        if rect.calc_area() > 100:
            print("this is big")
        elif rect.calc_area() > 1000:
            print("this is biggest")
        else:
            print("this is too small")

    # 클래스(클래스, 인스턴스) 공통의 변수를 쓰려고 할때
    @classmethod
    def print_count(cls):
        print(cls.count)

    def clear(self):
        self.width = 0
        self.height = 0

    def calc_size(self, values):
        sum = None

        if len(values) == 0:
            raise Exception("value is null")

        # try...except...else
        try:        # value
           sum = values[0] + values[1] + values[2]
        # except:  # 모든 exception을 잡음
        except IndexError as err:
            print('인덱스에러' + self._name)
        except Exception as err:
            print(str(err))
        else:
            print('에러없음')
        finally:
            print(sum)


def print_rectangle_info(rects):
    for _ in rects:                 # _ 가장 최근에 삽입된 변수를 나타 낸다. temp라는 변수는 사용안하기 위해서
        if _.color() == Color.BLUE:
            continue

        print(_.color())


# from module import * 로 사용되는 것은 모두 무시 private
def _make_rectangle(rect):
    print(rect.width, rect.height)


# private 모듈 메소드
def __clear_rect(rect):
    print('clear_rect')
    rect.clear()


# public 모듈 메소드
def clear_rect(rect):
    print('clear_rect')
    rect.clear()


# 가변 파라메터를 튜플로 리턴
def calc(*numbers):
    count = 0
    tot = 0

    for n in numbers:
        count += 1
        tot += n

    return count, tot
# result = calc(1, 2, 3, 4)
# print(result)
# print(str(result[0]) + str(":") + str(result[1]))
