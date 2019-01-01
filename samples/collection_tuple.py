import os


# Tupble을 사용하는 방법

# Tuple 정의
def define_tuple():
    t = ("AB", 10, False)
    print(t)


# 인덱싱 슬라이싱
def indexing_slising():
    t = (1, 5, 10)

    # 인덱스
    second = t[1]       # 5
    last = t[-1]        # 10

    # 슬라이스
    s = t[1:2]          # (5)
    s = t[1:]           # (5, 10)


# 병합과 반복
def combine_repeat():
    # 병합
    a = (1, 2)
    b = (3, 4, 5)
    c = a + b
    print(c) # (1, 2, 3, 4, 5)


# 변수 할당
def new_variable():
    name = ("hyomin", "bak")
    print(name) # ('hyomin', 'bak')

    firstname, lastname = ("hyomin", "bak")
    print(lastname, ", ", firstname) # bak, hyomin


