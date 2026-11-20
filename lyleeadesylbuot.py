class person:
   def__init__(self, name, age):
       self.name = name 
        self.age = age
person1 = person("Lina", 20)

print(f"name: {person1.name}, age: {person1.age}")




class person:
    def __init__(self, name, age):
         self.name = name 
         self.age = age

def get_age(self):
    return self.age 

person1 = person("Lina", 20)
print(f"name: {person1.name}, age: {person1.get_age()}")



class student(person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def study(self):
        print(f"{self.name} is studying {self.major}.")

student1 = student("Lina", 20)

print(f"name:{student1.name}")
print(f"age:{student1.get_age()}")student1.study()