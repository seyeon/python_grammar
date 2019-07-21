import os


def list_to_set():
    a = [1, 1, 2, 3, 4, 4, 5, 5]
    b = set(a)
    print(b)

def main():
    print("main")
    print("I have %s apples" % 3)
    print("This is a %s" % 3.332)
    name = '홍길동'
    age = 30
    print("나의 이름은 {name} 나이는 {age}")

    print("==========================")
    list_to_set()


if __name__ == '__main__':
    main()



