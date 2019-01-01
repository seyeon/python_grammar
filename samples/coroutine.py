import os
import asyncio
import random
import datetime


@asyncio.coroutine
def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(random.randint(0, 5))


