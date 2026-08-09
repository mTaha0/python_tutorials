class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 -100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_students):
        self.name = name 
        self.max_students = max_students
        self.students = []

    def addStudents(self,student):
        if len(self.students)  < self.max_students:
            self.students.append(student)
            return True
        return print(False)

    def get_avarage_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        if len(self.students) > 0:
            return value/len(self.students)
        return 0

    
student1 = Student("Taha",23,95)
student2 = Student("Mustafa",26,97)
student3 = Student("Emin",20,99)

course1= Course("science",2)
course1.addStudents(student1)
course1.addStudents(student2)
course1.addStudents(student3)
course1.get_avarage_grade()


        
