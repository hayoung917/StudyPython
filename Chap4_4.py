# numbers = [1,2,3,4,5,6]

# for i in reversed(numbers):
#     print("첫번쨰 반복문{} ".format(i))

# for i in reversed(numbers):
#     print("두번쨰 반복문{} ".format(i))

# example_list = ["itemA","itemB","itemC","itemD"]

# #단순출력
# print(example_list)
# print()

# #enumerate() 출력
# print(enumerate(example_list))
# print()

# #enumerate() list출력
# print(list(enumerate(example_list)))
# print()

# #반복문 조합
# for i, value in enumerate(example_list):
#     print("{}번째 요소는 {}".format(i,value))

# print()

# example_dict = {
#     "키A" : "값A",
#     "키B" : "값B",
#     "키C" : "값C",
#     "키D" : "값D"
# }

# #딕셔너리 아이템 함수
# print(example_dict.items())

# print()

# for key, element in example_dict.items():
#      print("dictionary[{}] = {}".format(key, element))

array = []
#빈 값 리스트 생성

#for문
for i in range(1,20,1):
    array.append(2**i)

#출력
print(list(array))
print()

array2 = [2**i for i in range(4,20)]
print(array2)

#조건활용리스트
array3 = ["사과","자두","초콜릿","바나나","체리"]
output = [fruit for fruit in array3 if fruit != "초콜릿"]
print(output)


