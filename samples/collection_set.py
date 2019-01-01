import os


# Set 정의
def define_set():
    # set 정의
    myset = {1, 1, 3, 5, 5}
    print(myset)  # 출력: {1, 3, 5}

    # 리스트를 set으로 변환
    mylist = ["A", "A", "B", "B", "B"]
    s = set(mylist)
    print(s)  # 출력: {'A', 'B'}


# Set 추가 삭제
def add_and_delete_set():
    myset = {1, 3, 5}

    # 하나만 추가
    myset.add(7)
    print(myset)

    # 여러 개 추가
    myset.update({4, 2, 10})
    print(myset)

    # 하나만 삭제
    myset.remove(1)
    print(myset)

    # 모두 삭제
    myset.clear()
    print(myset)


# Set 집합 연산
def operator_set():
    a = {1, 3, 5}
    b = {1, 2, 5}

    # 교집합
    i = a & b
    # i = a.intersection(b)
    print(i)

    # 합집합
    u = a | b
    # u = a.union(b)
    print(u)

    # 차집합
    d = a - b
    # d = a.difference(b)
    print(d)


# List

