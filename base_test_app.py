# 마지막 테스트 파이썬
import json

dic_mcu = []

# print(dic_mcu)
# with open("./data/mcu_movies.json", "w", encoding="UTF-8") as mcu_list:
#   json.dump(dic_mcu, mcu_list, ensure_ascii=False)

with open("./mcu_movies.json", "r", encoding="UTF-8") as mcu_list:
  dic_mcu = json.load(mcu_list)


# 문제 1번
# 페이즈가 1인 마블 시네마틱 유니버스 영화면 뽑기
#print(dic_mcu)

for item in dic_mcu:
  if item.get("시리즈") == '페이즈2':
      print("{}, {}".format(item.get("영화명"), item.get("개봉일")))


# 문제 2번
# 박스오피스가 450000000 이상인 영화들의 감독이름 리스트와 전체 합계금액, 평균 박스오피스 구하기

lists = []
direc = []
for item in dic_mcu:
    if item.get("박스오피스") >= 450000000:
        lists.append(item)
        direc.append(item.get("감독"))


get_sum = 0
for item in lists:
    get_sum += item['박스오피스']
direc = list(set(direc))
print("감독 리스트 : ", direc)
print('총 합 : ', get_sum)
print('평균 : ', get_sum/9)
