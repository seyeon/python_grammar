import os


# dictionary
# 정의하기
def define_dic1():
    scores = {"철수": 90, "민수": 85, "영희": 80}
    v = scores["민수"]  # 특정 요소 읽기
    scores["민수"] = 88  # 쓰기
    print(v)


# list또는 key=value로부터 dict를 생성하기
def define_dic2():
    # 1. Tuple List로부터 dict 생성
    persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
    mydict = dict(persons)

    age = mydict["홍대길"]
    print(age)  # 35

    # 2. Key=Value 파라미터로부터 dict 생성
    scores = dict(a=80, b=90, c=85)
    print(scores['b'])  # 90


# 추가 수정, 삭제 읽기
def add_modify_delete_read():
    scores = {"철수": 90, "민수": 85, "영희": 80}
    scores["민수"] = 88  # 수정
    scores["길동"] = 95  # 추가
    del scores["영희"]
    print(scores)
    # 출력 {'철수': 90, '길동': 95, '민수': 88}


# 한번에 여러개의 아이탬의 값을 변경하기
def update_dict():
    persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
    mydict = dict(persons)

    mydict.update({'홍대길': 33, '강찬수': 26})


# key, value 목록 빼내기
def dict_keys_values():
    scores = {"철수": 90, "민수": 85, "영희": 80}

    # keys
    keys = scores.keys()
    for k in keys:
        print(k)

    # values
    values = scores.values()
    for v in values:
        print(v)


# tuple list로 변환하기
def tuple_list():
    scores = {"철수": 90, "민수": 85, "영희": 80}

    items = scores.items()
    print(items)
    # 출력: dict_items([('민수', 85), ('영희', 80), ('철수', 90)])

    # dict_items를 리스트로 변환할 때
    itemsList = list(items)


# key 조회의 차이점
def get_dictkey_in():
    scores = {"철수": 90, "민수": 85, "영희": 80}
    v = scores.get("민수")  # 85
    v = scores.get("길동")  # None
    v = scores["길동"]  # 에러 발생

    # 멤버쉽연산자 in 사용
    if "길동" in scores:
        print(scores["길동"])

    scores.clear()  # 모두 삭제
    print(scores)









