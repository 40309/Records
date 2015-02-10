class StudentMark:
    def __init_(self):
        self.name = None
        self.mark = None


student_list = []
for count in range(2):
    #StudentMark = StudentMark()
    StudentMark.name = input("Name of student: ")
    StudentMark.mark = int(input("Enter Student's Mark: "))
    student_list.append(StudentMark.name)
    student_list.append(StudentMark.mark)
    

for each in range(1):
    print("Student Name: {0}".format(student_list[each]))
    print("Student Mark: {0}".format(student_list[each+1]))

print()

for each in range(1):
    print("Student Name: {0}".format(student_list[each+2]))
    print("Student Mark: {0}".format(student_list[each+3]))

        
