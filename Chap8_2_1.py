class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1

    @classmethod
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4 

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __lt__(self,value):
        return self.get_sum() < value.get_sum()

students = [
    Student("김가람",88,87,60,50),
    Student("이하영",90,87,20,50),
    Student("여예지",100,87,90,50),
    Student("백규현",60,87,30,50),
    Student("오동욱",28,80,60,50),
 ]

print('생성한 학생수 : ', Student.count)

# std_a = Student("김가람",88,87,60,50)
# std_b = Student("이하영", 89,50,60,74)

# print(std_a > std_b)

#print('Student 클래스 인스턴스 여부 : ', isinstance(std, Student))