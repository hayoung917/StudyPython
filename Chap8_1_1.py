def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

def student_get_sum(student):
    return student.get("korean") + student.get("math") + student.get("english") + student.get("science")

def student_get_avg(student):
    return student_get_sum(student) / 4

def student_toString(student):
    return "{}\t{}\t{}".format(student.get("name"), student_get_sum(student), student_get_avg(student))

students = [
    create_student("김가람",88,87,60,50),
    create_student("이하영",90,87,20,50),
    create_student("여예지",100,87,90,50),
    create_student("백규현",60,87,30,50),
    create_student("오동욱",28,80,60,50),
 ]

print("이름","총점","평균",sep='\t')

for student in students:
    #print("이름:{}, 한국어:{}".format(item.get("name"), item.get("korean")))
    score_sum = student_get_sum(student)
    score_avg = student_get_avg(student)
    print(student_toString(student)) 