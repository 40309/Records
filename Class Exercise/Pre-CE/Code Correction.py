#Tony K.
#2015-01-27
#Revision - Task 1

class student_name_and_mark():
    def __init__(self):
        self.name = None
        self.mark = 0

def student(student_list):
    for count in range(2):
        student_name_and_mark.name = input("Please enter student name: ")
        student_name_and_mark.mark = int(input("Please enter student mark: "))
        student_list.append(student_name_and_mark)
        print()

def display(student_list):
    print("Name   Mark")
    for count in range(2):
        #print("{0:10} {1:2}".format(student_list[count][0],student_list[count][1]))
        #print(student_list[count][0])
        #print(student_list[count][1])
    


#main program
student_list = []
student(student_list)
display(student_list)
#print(student_list)



        

