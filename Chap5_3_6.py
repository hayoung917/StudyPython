# def test():
#     print("A 지점 통과")
#     yield 1

#     print("B 지점 통과")
#     yield 2

#     print("C 지점 통과")

# output = test()

# print("D 지점 통과")
# a = next(output)
# print(a)

# print("E 지점 통과")
# b = next(output)
# print(b)

def num_gen():
    yield 1
    yield 2
    yield 3
    yield 4

print(list(num_gen()))

for i in num_gen():
    print(i)
