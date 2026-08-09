class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"köpeğin adı {name}, yaşı {age}'dir ")

    def barking(self):
        return "Hav Hav"

    def set_Name(self,name):
        self.name = name
        print(f"isim {name} olarak değiştirildi ! ")

dog1 = Dog("Karabaş",15)
print(dog1.barking())
dog1.set_Name("Maviş")
