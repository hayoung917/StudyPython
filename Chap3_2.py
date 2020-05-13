import datetime as dt

current = dt.datetime.now()
mon = current.month

if 3 <= mon <= 5:
    print("봄입니다")
elif 6 <= mon <= 8:
    print("여름입니다")
elif 9 <= mon <= 11:
    print("가을입니다")
else:
    print("겨울입니다")