import functools
from collections import OrderedDict
from datetime import datetime


def cache(max_limit=10):
    def internal(f):
        @functools.wraps(f)
        def deco(*args):

            # print(deco._cache)
            # print(deco._uses)
            if args in deco._cache:
                # Если по более раннему времени использованого
                deco._uses[args] = datetime.now()
                # Если по минимальному количеству использований
                # deco._uses[args] += 1
                return deco._cache[args]

            result = f(*args)

            if not len(deco._cache) < max_limit:
                deco._cache.pop(min(deco._uses, key=deco._uses.get))
                deco._uses.pop(min(deco._uses, key=deco._uses.get))
            deco._cache[args] = result
            # Если по более раннему времени использованого
            deco._uses[args] = datetime.now()
            # Если по минимальному количеству использований
            # deco._uses[args] = 1

            return result

        deco._cache = {}
        deco._uses = {}

        return deco
    return internal



def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args):
            if args in deco._cache:
                deco._cache.move_to_end(args, last=True) # Перемещение только что использованного элемента в конец списка на удаление
                return deco._cache[args]
            result = f(*args)
            # Удаление из словаря значения, если в нем больше чем задано max_limit. Для Домашнего задания
            if len(deco._cache) >= max_limit:
                deco._cache.popitem(last=False) # Использование collections.OrderedDict чуть укоротило код - все так же удаление первого элемента
            deco._cache[args] = result
            return result
        deco._cache = OrderedDict()
        return deco
    return internal