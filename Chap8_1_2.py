class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4 

    def toString(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())

#student = Student()    
students = [
    Student("김가람",88,87,60,50),
    Student("이하영",90,87,20,50),
    Student("여예지",100,87,90,50),
    Student("백규현",60,87,30,50),
    Student("오동욱",28,80,60,50),
 ]

print("이름","총점","평균",sep='\t')

for student in students:
    print(student.toString())