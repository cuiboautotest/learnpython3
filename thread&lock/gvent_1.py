# gevent
import gevent


def foo():
    print("Running in foo")
    gevent.sleep(0)
    print("Explicit context switch to foo angin")


def bar():
    print("Explicit context to bar")
    gevent.sleep(0)
    print("Implicit context swich back to bar")


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])