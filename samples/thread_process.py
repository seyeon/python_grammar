from time import sleep, ctime
import threading
from multiprocessing import Process, Queue
import time


# Python의 Thread는 GIL때문에 I/O를 제외한 부분에서의 성능 향상은 전혀 없다.
# 이때는 차라리 Process를 분리 해서 하는 것이 더 낫다.
# 다만 process로 분리를 하게 되면 해당 연산간 값의 쉐어가 불가능 하다.

def work(start, end, result):
    total = 0

    for i in range(start, end):
        total += 1

    result.append(total)
    return


def work(start, end, tag, result):
    total = 0

    for i in range(start, end):
        total += 1
        print("{} Total is {}".format(tag, total))

    result.append(total)


def run_thread():
    START, END = 0, 1000000000

    result1 = list()
    result2 = list()
    result3 = list()

    th1 = threading.Thread(target=work, args=(START, END//2, "Thread 1", result1))
    th2 = threading.Thread(target=work, args=(START, END//2, "Thread 2", result2))
    th3 = threading.Thread(target=work, args=(START, END//2, "Thread 3", result3))
    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()

    print("Result: {}".format(result1))
    print("Result: {}".format(result2))
    print("Result: {}".format(result3))


def run_process():
    START, END = 0, 1000000000

    result = Queue()
    pr1 = Process(target=work, args=(START, END//2, result))
    pr1.start()
    pr1.join()

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp


loops = [8,2]


class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self,name=name)
        self.func = func
        self.args = args

    def run (self):
        self.func(*self.args)
        # 함수를 받아서 처리하는게 아니라 여기에 직접 구현하는 경우가 일반적..


def loop(nloop,nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'at:', ctime())


def test():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i,loops[i]),loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all Done at: ', ctime())


def get_current_millisecond():
    return int(round(time.time() * 1000))


def run_thread(start, stop, tag, result):
    start_time = get_current_millisecond()
    print("Begin:" + tag + " = " + str(start_time))

    value = 0

    for i in range(start, stop):
        value += i
        result.append(value)

    end_time = get_current_millisecond()
    print("end:" + tag + " = " + str(end_time))
    print("spend time:" + tag + " = " + str(end_time - start_time))


if __name__ == '__main__':
    START = 0
    STOP = 100000000

    # th1 = Thread(target=run_thread, args=(START, STOP//2, "Th1", list()))
    # th1.start()

    th1 = Process(target=run_thread, args=(START, STOP//2, "Th1", list()))
    th1.start()

 #   test()
