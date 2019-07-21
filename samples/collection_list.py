import os


# 선언
def defined_list():
    a = []  # 빈 리스트
    a = ["AB", 10, False]

    a = ["AB", 10, False]
    x = a[1]  # a의 두번째 요소 읽기
    a[1] = "Test"  # a의 두번째 요소 변경
    y = a[-1]  # False


# list slicing
def slice_list():
    a = [1, 3, 5, 7, 10]
    x = a[1:3]  # [3, 5]
    x = a[:2]  # [1, 3]
    x = a[3:]  # [7, 10]


# 추가, 수정, 삭제
def add_modify_delete():
    a = ["AB", 10, False]
    a.append(21.5)  # 추가
    a[1] = 11  # 변경
    del a[2]  # 삭제
    print(a)  # ['AB', 11, 21.5]


# 병합 반복
def combine_loop():
    # 병합
    a = [1, 2]
    b = [3, 4, 5]
    c = a + b
    print(c)  # [1, 2, 3, 4, 5]

    # 반복
    d = a * 3
    print(d)  # [1, 2, 1, 2, 1, 2]


# 검색
def search_list():
    mylist = "This is a book That is a pencil".split()
    i = mylist.index('book')  # i = 3
    n = mylist.count('is')  # n = 2
    print(i, n)


# 응용하기
def comprehension():
    item_list = [n ** 2 for n in range(10) if n % 3 == 0]
    print(item_list)
    # 출력: [0, 9, 36, 81]


# iterator
# 반복자를 사용할 수 있다.
def iter_test():
    it = [1, 2, 3].__iter__()
    it.__next__()


# iterator를 리턴한다.
# itr = number_itr_generator()
# a = next(itr)     # 0 출력
def number_itr_generator():
    yield 0
    yield 1
    yield 2
    yield 3



    