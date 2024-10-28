#1
class Student:
 print("Hi")
first_student = Student()
#2
class Student:
 print("Hi")
 def __init__(self):
  self.height = 160
 print("I am alive!")
first_student = Student()
#3
class Student:
 print("Hi")
 def __init__(self):
   self.height = 160
   print(self)
first_student = Student()
#4
class Student:
 def __init__(self):
  self.height = 160
nick = Student()
print(nick.height)
#5
class Student:
 def __init__(self, height=160):
  self.height = height
nick = Student()
kate = Student(height=170)
print(nick.height)
print(kate.height)
#6
class Student:
  amount_of_students = 0
  def __init__(self, height=160):
   self.height = height
   Student.amount_of_students = Student.amount_of_students + 1
nick = Student ()
kate = Student(height=170)
print(nick.amount_of_students)
print(Student.amount_of_students)
#7
class Student:
 height = 160
 def __init__(self):
  print(self.height)
nick = Student()
#8
class Student:
 height = 160
 def __init__(self):
  print(self.height)
  self.height+=10
nick = Student()
kate = Student()
#9
class Student:
 def __init__(self):
  self.height = 170
 height = 160
 def printer(self):
  print(self.height)
nick = Student()
nick.printer()
#10
class Student:
 amount_of_students = 0
 def __init__(self, height=160):
  self.height = height
 Student.amount_of_students=Student.amount_of_students+1
 def grow(self, height=1):
  self.height+=height
nick = Student()
kate = Student(height=170)
nick.grow(height=15)
print(kate.height)
print(nick.height)
def __str__(self):
    return f"I am a student.
            My name is {self.name}."
nick = Student(name = "Nick")
print(nick)
#11

#12
