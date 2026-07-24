class Student:
    def __init__(self,name,age): #init - это метод, конструктор по которому будут строиться объекты на базе класса(чертежа)
        self.name = name #присваивает конкретному студенту конкретный параметр
        self.age = age

student1 = Student("Anna",20)
student2 = Student("Bob",22)


print(student1.name,student1.age)
print(student2.name,student2.age)