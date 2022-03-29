
def evn(n):
    if n%2==0:
        return n
    else:
        return f"{n} odd num "
print(evn(8))
print()
print()
# l = [2, 3, 5, 6, 7, 8]
# e_o = lambda num: "{num} is even" if num % 2 == 0 else "{n} odd num "
# y = map(e_o, l)
# print(list(y))
#
# def evn1(n):
#   for i in l:
#     if n%2==0:
#         return n
#
# print(list(filter(evn1,l)))

def square(n):
    return n**2

l=[2,3,4,5]
res=""
for item in l:
    print(square(item))
#     res.append(x)
# sqr=lambda n:n**2
# print(sqr(3))
print(list(map(square,l)))

print()

# def rev(s):
#     if len(s)==0:
#         return s
#     else:
#         return rev(s[1:])+s[0]
# print(rev("hello"))
#
# # def rev(st,ed):
# #   if st<=ed:
#     return
#   print(st-1,ed)
#   rev(st-1,ed)
# rev(10,1)
# def last(sequ):
#  return last(sequ[:-1])
# print(last("hai"))
# l1=["hai","hello"]
# l2=[10,20]
# def concat1(ll1,ll2):
#  # l1=["hai","hello"]
#  # l2=[10,20]
#  d={}
#  for i in range(len(l1)):
#     d[l1[i]]=l2[i]


# print(concat1(l1,l2))
#
def fib1(n):
    if n<1:
        return n
    else :
        return fib1(n-1)+fib1(n-2)

    n=5
    if n<=0:
        print("invalid")
    else:
     for i in range(n):
             print(fib1(i))



