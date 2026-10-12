class Student:
    def __init__(self,name,age,course,marks):
        self.name=name
        self.age=age
        self.course=course
        self.marks=marks
    
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("course:",self.course)
        print("marks:",self.marks)
        print("------------------")

students=[]
n=3
def add_student():
    for i in range(3):
       print("enter details of student",i+1)
       name=input("enter name:")
       age=int(input("enter age:"))
       course=input("enter course name:")
       marks=int(input("enter marks:"))

       student=Student(name,age,course,marks)
       students.append(student)
def display_students():

    print("====student details=====")

    for student in students:
     student.display()
def search_student():
    search_name=input("enter name to search:")
    found=False
    for student in students:
     if student.name==search_name:
        print("student found")
        student.display()
        found=True
        break
    if found==False:
        print("student not found")

def delete_student():
    delete_name=input("enter name to delete:")
    found=False
    for student in students:
      if student.name==delete_name:
        students.remove(student)
        print("student deleted successfully")
        student.display()
        found=True
        break
    if found==False:
      print("not deleted")

def update_student():
    update_name=input("enter name to update:")
    found=False
    for student in students:
       if student.name==update_name:
        print("student found")
        student.age=int(input("enter new age:"))
        student.course=input("enter new course name:")
        student.marks=int(input("enter new marks:"))

        print("student updated successfully")
        found=True
        break 
    if found==False:
        print("student not updated")

while True:
    print("=====studenet management system=====")
    print("1.add student")
    print("2.display students")
    print("3.search student")
    print("4.delete student") 
    print("5.update student")
    print("6.exit")
    choice=input("enter choice:")
    if choice=="1":
       add_student()
    elif choice=="2":
       display_students()
    elif choice=="3":
       search_student()
    elif choice=="4":
       delete_student()
    elif choice=="5":
       update_student()
    elif choice=="6":
       print("program ended")
       break
    else:
       print("invalid choice")

    