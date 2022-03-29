#####################################3
# def fib1(n):
#     if n<1:
#         return n
#     else :
#         return fib1(n-1)+fib1(n-2)
#
# fib1(5)
# #
# #####################################################################
# """"""
# def is_prime(number):
#
#     for i in range(2, number):
#         if number % i == 0:
#             print(f"{number} is not prime")
#             break
#
#     else:
#         print(f"Number {number}is prime")
#
# is_prime(12)
# """"""


# def fib1(n):
#     if n <= 1:
#         return n
#     else:
#         return fib1(n - 1) + fib1(n - 2)
#
#
# n=5
# if n<=0:
#
#     "invalid"
# else:
#     for i in range(n):
#         print(fib1(i))
#
# def cnt1(n):
#      if n<=10:
#        print(n)
#        cnt1(n+1)
#      else:
#         69
#
# cnt1(1)

# def spam():
#     c=10
#     def wrapper():
#         b=20
#         nonlocal c
#         c+=10
#         print(c)
#     wrapper()
# spam()

# def recursive_fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))
#
#
# n_terms = int(input("enter the range of fibonacci series: "))
# # check if the number of terms is valid
# if n_terms < 0:
#     print("Invalid input ! Please input a positive value")
# else:
#     print("Fibonacci series:")
#     for i in range(n_terms):
#         print(recursive_fibonacci(i))

# l = ["gmail", "google", "instagram", "facebook", "yahoo"]
# def odd_(string):
#     if len(string)%2==1:
#         return string
#
# print(list(filter(odd_,l)))

# a, *, b=[1,2,3,4]
# print(a, *, b)
# #
# # l = [98, 14, 62, 17, 56, 1, 5, 96]
# # n=5
# # for _ in range(len(l)-1):
# #     for i in range(len(l)-1):
# #         if l[i] > l[i+1]:
# #             l[i], l[i+1] = l[i+1], l[i]
# # print(l[-n])
# # l = [98, 14, 62, 17, 56, 1, 5, 96]
# # n = 5
# # for _ in range(len(l)-1):
# #     for i in range(len(l)-1):
# #         if l[i] > l[i+1]:
# #             l[i], l[i+1] = l[i+1], l[i]
# # print(l[-n])
# #
# # sentence = "python is a programming language"
# # l = sentence.split()
# #
# # for _ in range(len(l)-1):
# #     for i in range(len(l) - 1):
# #         if len(l[i]) > len(l[i+1]):
# #             l[i], l[i+1] = l[i+1], l[i]
# # print(l[-1])
# # print(l)
# # print()
# # print()
# # #nth smallest number
# #
# # l = [98, 14, 62, 17, 56, 1, 5, 96]
# # n = 5
# # for _ in range(len(l)-1):
# #     for i in range(len(l)-1):
# #         if l[i] < l[i+1]:
# #             l[i], l[i+1] = l[i+1], l[i]
# # print(l[-n])
# # print(l)
# # # longest non repeated word
# # sentence = "python is a programming language and programming is fun"
# # l = sentence.split()
# # max_word = ""
# # #
# # # for word in l:
# # #     if len(word) > len(max_word) and l.count(word) == 1:
# # #         max_word = word
# # # print(max_word)
# # # l = [98, 14, 62, 17, 56, 1, 5, 96]
# # # n=5
# # # for _ in range(len(l)-1):
# # #     for i in range(len(l)-1):
# # #         if l[i] > l[i+1]:
# # #             l[i], l[i+1] = l[i+1], l[i]
# # # print(l[-n])
# # #
# # # l = [98, 14, 62, 17, 56, 1, 5, 96]
# # #
# # # for _ in range(len(l)-1):
# # #     for i in range(len(l)-1):
# # #         if l[i] > l[i+1]:
# # #             l[i], l[i+1] = l[i+1], l[i]
# # # print(l)
# # # print()
# # # a=10
# # # print(a)
# # #
# # # def fub():
# # #     a=10
# # #     print(a+10)
# # #     fub()
# # #     print(a)
# # #
# # #     print()
# # # a = 1
# # # print(id(a))
# # # def fun():
# # #     global a
# # #     a = a + 1
# # #     print(a)
# # #
# # # fun()
# # # print(a)
# # #
# # # print()
# # # a = 10
# # # print(a)
# # #
# # # def fub():
# # #  a = 10
# # #  print(a + 10)
# # # fub()
# # # print(a)
# # #
# # print()
# # print()
# # words=['apple',"google","gmail",'google','apple','google','flipkart']
# # d={}
# # for word in words:
# #     if word not in d:
# #         d[word]=1
# #     else:
# #         d[word]+=1
# # print(word)
# # res=sorted(d.items(),key=lambda item:item[1])
# # # least_common,*rest,most_common=res
# # # print(most_common)
# # print(res)
# # print()
# # print()
# #
# #
# #
# #
# # sentence="today is holiday but we are in class even afternoon we will be in class"
# # words=sentence.split()
# # d={}
# # for word in words:
# #     if len(word) not in d:
# #         d[len(word)]=[word]
# #     else:
# #         d[len(word)]+=[word]
# # print(d)
# # r=sorted(d.items())
# # s,*rs,l=r
# # print(s)
# # print(l)
# print(r)
print()
print()
# s="hi good morning"
# l=s.split()
# print(list(map(len,l)))
# def upper1(n):
#     return n.upper()
# print(list(map(upper1,l)))
# l=[1,2,3,4]
# def power(num):
#     index,item=num
#     return item**index
# print(list(map(power,enumerate(l))))

# s="apple orange banan"
# x=s.split()
# def vowels(sttn):
#     if sttn[0].lower() in 'aeiou':
#         return sttn
# print(list(filter(vowels,x)))

# l=[2,-3,-4,-5]
# convert=lambda num:abs(num)
# print(list(map(convert,l)))
# print(list(map(abs,l)))

#highest value
# d = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "FB": 10.75, "HPQ": 37.20}
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])

# d = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "FB": 10.75, "HPQ": 37.20}
# res = sorted(d.items(), key=lambda item: len(item[0]))
# print(dict(res))
# d = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "FB": 10.75, "HPQ": 37.20}
# res = sorted(d.items(), key=lambda item: len(item[0]))
# print(dict(res))
# sort based on length
sentence = "python is a programming language and programming is fun"
words = sentence.split()
d = {}
d = {word: len(word) for word in words }
res = sorted(d.items(), key=lambda item: len(item[0][1:4]))
print(dict(res))
