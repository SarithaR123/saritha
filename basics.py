def spam(func):
    def wrapper(*args, **kw):
        print('in wrapper')
        return func(*args, **kw)

    return wrapper


@spam
def add(a, b):
    return a + b


print(add(1, 2))

