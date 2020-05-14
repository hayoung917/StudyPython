# import sys
# print(sys.argv)

# print(sys.getwindowsversion())
# print(sys.copyright)
# print(sys.version)

import os
import sys
import datetime
from urllib import request,response

print("OS : ",os.name)
print("폴더 : ",os.getcwd())
print("files : ", os.listdir())

# os.mkdir("hello")
# os.rmdir("hello")
# os.system("dir")
current = datetime.datetime.now()
print("{}년 {}월 {}일 {}시 {}분 {}초 {}ms".format(
    current.year,
    current.month,
    current.day,
    current.hour,
    current.minute,
    current.second,
    current.microsecond

))

target = request.urlopen("https://www.google.com")
# output = target.read()
# print(output)
# status = target.getheaders()

# for item in status:
#     print(item)

print(target.status)