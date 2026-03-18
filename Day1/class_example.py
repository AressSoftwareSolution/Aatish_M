# classes and objects

# class student:
#     name="Aatish"
#     Age =22
#     Education="BE"
#     def info (self):
#         print(f"{self.name} is a {self.Age} years old.")

# s = student()

# s.info()


class person:
    def info(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your Age: "))
        self.education = input("Enter your education: ")
        self.address = input("Enter your address: ")

    def display(self):
        print("My name is: " , self.name)
        print("My age is: ", self.age)
        print("My education is: ", self.education)
        print("My address is: ", self.address)

p1 = person()
p2 = person()
p1.info()
p1.display()
p2.info()
p2.display()
