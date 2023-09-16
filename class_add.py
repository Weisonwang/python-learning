class Student:
    def __init__(self,name,student_id):
        self.name = name #self.name说明是绑定到对象身上的属性,name只是一个普通的变量，它的值是参数传进来的
        self.student_id = student_id
        self.grades = {"语文":0,"数学":0,"英语":0}
    def Set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade
    def print_grades(self):
        print(f"学生{self.name},(学号:{self.student_id})的成绩为")
        for course in self.grades:
            print(f"{course}:{self.grades}分")
chen = Student("陈e","22341222")
chen.Set_grade("数学",93)
chen.Set_grade("英语",91)
print(chen.name)
print(chen.grades)