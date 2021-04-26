#OOP (Object Oriented Programming) - Classes & Objects
class Student():
    #class Attributes


    def __init__(self, name , age, clg):
    #instance Attributes
        self.name_attr = name
        self.age_attr = age
        self.clg_attr = clg
    def show(self):
        print("Student {}'s showing details....".format(self.name_attr))
        print("Name: " + self.name_attr + "\nContact: " + self.age_attr + "\nCollage Name :" + self.clg_attr)
    def upmarks(self,new_marks):
        self.marks_attr = new_marks




#Main
print("Enter 3 Student Details...")
#student 1
print("\nEnter Student 1 details")
a1 = input("Enter Name of Student :-")
b1 = input("Enter contact of student :-")
c1 = input("Enter Collage Name :-")
student1 = Student(a1,b1,c1)

#student 2
print("\nEnter Student 2 details")
a2 = input("Enter Name of Student :-")
b2 = input("Enter contact of student :-")
c2 = input("Enter Collage Name :-")
student2 = Student(a2,b2,c2)

#student 3
print("\nEnter Student 3 details")
a3 = input("Enter Name of Student :-")
b3 = input("Enter contact of student :-")
c3 = input("Enter Collage Name :-")
student3 = Student(a3,b3,c3)


#printing details
print("Details of Student")



student1.show()
student2.show()
student3.show()


print("\n\n<O>......<0>......<O>")
