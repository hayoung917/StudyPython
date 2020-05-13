format_a = "{}".format(1000000);
format_b = "{} {}".format(100,200,300,400);

format_c = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)

output_a = "{:010d}".format(30)
output_b = "{:010.4f}".format(3.141592)
output_c = "{:g}".format(52.0)

input_s = "Hello Python Programming!!"
input_t = """
     안녕하세요     
테스트입니다.     
"""

check_str = "TrainA10"
check_str1 = "안녕하세요"

print(check_str1.find("요"))

print(check_str.isalnum())

print(input_s.upper())
print(input_s.lower())
print(input_t.strip())

print(format_a)
print(format_b)
print(type(format_b))

print(format_c)

print(output_a)
print(output_b)
print(output_c)