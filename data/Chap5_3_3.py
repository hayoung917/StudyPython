#파일 열기
f = open("./data/basic.txt","w")
#파일쓰기
f.write("Hello Python Programming...!!!")
#파일닫기
f.close()

f1 = open("./data/basic.txt","a")

f1.write("\nAdded documents")

f.close()

with open("./data/test.txt","w") as f3:
    f3.write("With sentence document")

with open("./data/test.txt","r") as f4:
    content = f4.read()
print(content)
