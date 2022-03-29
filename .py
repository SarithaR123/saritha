# # greatest of 2 numbers
# m = 5
# n = 10
# p = 7
#
# if (m > n)  and (m > p):
#     print("m is greater num")
# elif n > p:
#     print("n is  greater num : ",n)
# else:
#     print("p is greater")
# print()
# s="eve"
# d={}
# #d[key]=value
# d[s]=len(s)
# print(d)
#b=a
a=[1,2,[3]]
b=[1,2,[3]]
# b=a[::]
# print(a[::])
print(a==b)
print(id(a)==id(b))
print(a is b)
print(a is not b)
# print(id(a))
# print(id(b))

# print()
# a=4
# if a%2==0:
#     print(f"{a} is an even number")
# else:
#     print(f"{a} is odd number")
# print()
# #even length or not
# s="hello"
# if len(s)%2==0:
#    print("iterable is even number of elements")
# else:
#    print("iterabel is odd num of elements")
# x=int(input("enter value of x"))
# y=int(input("enter value of y"))
# print(type(x),type(y))
# if x > y:
#     print("x is greater ")
# else:
#     print("y is greater")
# print()
# s="hello"
# if s[::-1] == s:
#     print(f"{s} is palindrome")
# else:
#     print(f"{s} is not palindrome")p
# print()
# s="apple"
# if s[0] in "aeiouAEIOU" :
#     print("string is starting with vowel")
# else:
#     print("string is not starting with vowel")
# print()
# n=1221
# x=str(n)
# if x[::-1] == x:
#     print(f"{n} is palindrome")
# else:
#     print(f"{n} is not palindrome")
# s="apple"
# if s[-1] in "aeiouAEIOU" :
#     print("string is end with vowel")
# else:
#     print("string is not ending with vowel")

# print()
# print()
# char="B"
# if "a" <= char <= "z":
#     upr=chr(ord(char)-32)
#     print(upr)
# elif "A" <= char <= "Z":
#     print(chr(ord(char)+32))
# else:
#     print("char is not an alphabet")
print()


# sentence = "hai good afternoon welcome to pyhon"
# d = {}
# words = sentence.split()
# for word in words:
#         if word[0] not in d:
#             [d[word]] = [words]
#         print(d)
# else:
#     d[words[0]].append(word)

# print()
# s="hello hai hello hai"
# d={}
# for char in s:
#     if s.count(char)>1:
#         print(char,end="")
# print()

# print()
# s = "hello hai hai hello how are you how are you hai hello "
# d = {}
# words = s.split()
# for i in range(len(words)):
#     d[i]=words[i]
#
#     print(d)
# print()
# print()
# l1=["hello","world"]
# l2=[10,20]
# d={}
# for i in range(len(l1)):
#     d[l1[i]]=l2[i]
#     print(d)
#     print()
#     d1={}
#     for item1,item2 in zip(l1,l2):
#         d1[item1]=item2
#         print(d1)
# s="hello"
# res=""
# for char in s:
#     res=char+res
#     print(res)
print()
s=" hai  you how are you  "
d={}

words=s.split()
for word