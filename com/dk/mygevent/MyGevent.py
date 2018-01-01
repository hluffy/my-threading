import gevent
"""gevent协程自动切换"""

def test1():
    print('this is test11')
    gevent.sleep(2)
    print('this is test12')


def test2():
    print('this is test21')
    gevent.sleep(1)
    print('this is test22')


gevent.joinall([
    gevent.spawn(test1),
    gevent.spawn(test2),
])