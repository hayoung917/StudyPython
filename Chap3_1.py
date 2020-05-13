# #입력
# number = input("수를 입력하세요 : ")
# number = int(number)

# # 양수조건
# if (number > 0):
#     print("양수입니다")
# elif(number < 0):
#     print("음수입니다")
# else:
#     print("0입니다")

import datetime

current = datetime.datetime.now()

print(current.year, current.month, current.day)
print(current.hour,"시",current.minute,"분",current.second,"초")
print("{}년 {}월 {}일 {}시 {}분 {}초".format(current.year,current.month,current.day,current.hour,current.minute,current.second))

number = input("수 입력 : ")
last_ch = number[-1]

if last_ch in "1220":
    print("짝수")