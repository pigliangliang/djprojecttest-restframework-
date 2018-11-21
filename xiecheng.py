#author_by zhuxiaoliang
#2018-11-17 上午10:40

#协程例子
"""



import asyncio
import functools
import time

now = lambda: time.time()


async def do_something_word(x):
    print('writing:',x)
    await asyncio.sleep(x)
    print('after {} done'.format(x))

def callback(t,future):
    print('callback:',t,future.result())

start = now()

coroutine1 = do_something_word(2)
coroutine2 = do_something_word(1)
coroutine3 = do_something_word(0)


tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3),
]

loop = asyncio.get_event_loop()

for task in tasks:
    task.add_done_callback(functools.partial(callback,2))
loop.run_until_complete(asyncio.wait(tasks))

print('*'*20)
for task in tasks:
    task.add_done_callback(functools.partial(callback, 2))
    print('Task return: {}'.format(task.result()))


"""


#装饰器 functools.wraps示例
"""

#functools.wraps 保证被装饰的对象的属性不被装饰器改变。
import functools
def outerone(*args):
    print('参数是：',*args)
    out = args[0]
    @functools.wraps(out)
    def outertwo(func,*args,**kwargs):
        @functools.wraps(func)
        def inner(*args,**kwargs):
            print(out)
            result = func(*args,**kwargs)
            return result
        return inner
    return outertwo

@outerone('dfdf')
def f():
    print(f.__name__)

f()

"""

