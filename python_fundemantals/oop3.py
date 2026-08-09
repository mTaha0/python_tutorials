#parent-child classes

class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def  show(self):
        print(f"i am {self.name} and i am {self.age} years old")

    def speak(self):
        print("i dont know what to say ! ")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        print(f"{color}")

    def speak(self):
        print("meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("minno",25)

a = Cat("taha",20,"mavi")
print(a.name)