# # # from builtins import type
# # #
# # #
# # # x=18
# # # print(type(x))
# # #
# # # "type()"
# # # z=1+2j
# # # print(type(z))
# # #
# # # string="hi welcome to python"
# # # print(string[: :-2])
# # #
# # # print(yo)
# # s1="haii"
# # i=0
# # while i<len(s1):
# #  print(s1[i])
# #  i+=1
# def log(func):
#  def wrapper(*arg,**kw):
#    print(func,__name__)
#    return func(*arg,**kw)
#  return wrapper
# X=0123
# print(X)
# a=100
# b=a
# print(isinstance(1+2j,(int,float,bool)
# k=print(complex(2,3))
# string="fast andf urious 3"
# print(string.isalnum())
# list1=[1,2,3]
# list2=list1.copy()
# print(list2==list1)
# string="mary had a little lamb"
# # print(string[:-3])
# avengers=["iron man","thanos","captain america","thor"]
# print(avengers.pop(1))
# string="Twinkle twinkle little star"
# print(string[-2:-5])
# list_of_words=["mary","had","a","little","lamb"]
# list_of_words.sort()
# print(list_of_words)
# print(list_of_words.sort())
# nam=['apple','oer','mn',"cmd"]
# nam.sort()
#
# print(nam)
# string="Today is Friday"
# string.split(2)
# li=[10,1,9,2,8,3,7,4,6]
# li.sort()
# print(li)
sentence="Everyone must have felt"
print(sentence.find("thor"))
word="Corona one".split()
# a=word.split()
print(word)
str1="python"
print(str1[2])
str1="x"
print(str1[0:9])
la=["Py","c++","ja","pe","ru"]
res=la[2:4]
print(type(res))
t=2^63
print(t)
names=["Ha Po","Du","vo"]
names.extend(["Ron"])
print(names)
names.append(["Ron"])
print(names)
la=["py,","c++","ja","pe","Ru"]
print(la.pop(-3))
sentence="How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
print(sentence.rindex("chuck"))
d1={"one": 1, "Two": 2, "three": 3, "Four": 4}
print(dict.fromkeys(d1))
print(dict.fromkeys(la,0))
s="hello"
print(dict.fromkeys(s))
l=[1,2,3,4]
print(dict.fromkeys(l))
print()
d1={"on":1, "Tw":2,"th" :3,"fo":4}
d2={"th":5, "fi":5, "Tw":4}
print({**d1, **d2})
print()
d1={"a":1, "b": 2}
d2={"c": 3,"d": 4}
print({*d1, *d2})
a={1, 2, 3, 4}
b={4, 3, 6, 7}
a.symmetric_difference(b)
print(a)
l1=[[1,2],[3,4],[5,6]]
print(dict(l1))
l1=["ab","12","cd"]
# print(dict(l1))
# s={1,2,3}
# print(d2.popitem())
# print(d2)
# print(d1.pop('b'))
# s="abc"
# print(list(s))
# print(tuple(s))
# print(set(s)
# print(dict(s))
l=[1,2,3]
print(set(l))
print(tuple(l))
# print(dict(s))
print(str(l))
print()
l={1,2,3}
print(list(l))
print(tuple(l))
# print(dict(s))
print(str(l))
l1=[1,2,3]
l2=[1,2,3]
print(l1+l2)
print(*l1,*l2)
print()
d1={"a":1, "b": 2}
print(str(d1))
# print(list(d1))
# print(tuple(d1))
# print(set(d1))
# print()
# s1=10
# print(int(s1))
# print(float(s1))
# print(complex(s1))
# print(bool(s1))
# print()
a={1,2,3,4}

b={3,4,5,6}
print(a.union(b))
print(a)
print(a.update(b))