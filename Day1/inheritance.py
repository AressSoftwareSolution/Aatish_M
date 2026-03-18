class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person(self):
        print(f"Person's name is {self.name} and age is {self.age}")

class student(person):
    def __init__(self, name, age, course):
        self.name = name
        self.age=age
        self.course=course
    def display_student(self):
        print(f"Course is: {self.course}")


p = person("Aatish",22)
s = student("Tushar",22,"BE")
s.display_person()
s.display_student()