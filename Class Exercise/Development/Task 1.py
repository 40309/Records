#Tony K.
#02/02/2014
#Development Exercise - Task 1

class students:
    def __init__(self):
        self.name = None
        self.module = None
        #self.module2 = None
        #self.module3 = None
        #self.module4 = None

student = students()
student_list = [
    [],
    [],
    [],
    [],
    []
    ]
for count in range(2):
    student.name = input("Please enter student name: ")
    student_list.insert(count, student.name)
    for count in range(4):
        student.module = int(input("Please enter your module mark: "))
        student_list.insert(count, student.module)
print(student_list[0])
        
        
        
        
        

