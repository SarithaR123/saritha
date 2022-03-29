# from builtins import type
#
#
# x=18
# print(type(x))
#
# "type()"
# z=1+2j
# print(type(z))
#
# string="hi welcome to python"
# print(string[: :-2])
#
# print("youtube.txt"[:7])
# print(
def spam(func):
    def wrapper(*args,**kw):
        print('in wrapper')
        return func(*args,**kw)
    return wrapper
@spam
def add(a,b):
    return a+b

print(add(1,2))

