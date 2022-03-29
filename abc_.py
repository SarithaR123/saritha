# import os
#
# print(os.getcwd())
#
# path =os.chdir(r"C:\Users\Vidyashree M C\PycharmProjects\Alpha4\files")
# print(os.listdir(path))
#
# # using len()
# os.chdir(path)
# print(os.getcwd())
# # with open("sample.txt") as file:
# #     ch_count = 0
# #     for line in file:
# #         ch_count += len(line)
# # print(ch_count)
# # #
# # print(os.getcwd())
# # os.mkdir("sample")
# # path = r"C:\Users\Admin\PycharmProjects\Alpha\abc_.py"
# # # changing the directory
# # os.mkdir("sample")
# # # os.chdir(path)
# # print(os.getcwd())
# # # # # creating folder
# # # # os.mkdir("sample")
# # # #
# # # # # delete folder
# # os.rmdir("sample")
# # #
# #
# # # with open("sample.txt","w") as file:
# # #     ch_count = 0
# # #     for line in file:
# # #         ch_count += len(line)
# # # print(ch_count)
def spam(fnc):
    def wrapper(*args,**kw):
        print('in wrapper')
        return fnc(*args,**kw)
    return wrapper

@spam
def add(a,b):
    return a+b

print(add(1,2))