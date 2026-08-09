class Parent:
    #sınıf değişkenleri
    borc = 1000
    kredi = 2000

    all = [] # oluşturulan nesneleri eklemek için liste oluşturduk 
    
    def __init__(self,name,age,kimlik,money=5000):

        #argümanları kontrol edelim
        assert money >= 5000, f"Para 'den büyük olmalıdır"
        assert age >= 0
        assert isinstance(kimlik,int), "Kimlik sayı olmalıdır"

        #nesne değişkenleri
        self.name = name
        self.age = age
        self.money = money
        self.kredi = Parent.kredi # burada nesneye bağımsız bir kredi atamış olduk
        self.__kimlik = kimlik
        Parent.all.append(self) # nesneleri listeye eklememizi sağlar

    @classmethod
    def borc_faizi(cls):
        cls.borc += cls.borc*(0.5) #cls iel tanımladığım için tanımladığım sınıfa ait olur, Child.borc olarak düşünülebilri
        return cls.borc

    @staticmethod
    def say_hello():
        return print("Merhabalar")

    def __repr__(self):
        return f"Nesne( 'adı': {self.name}, 'yaşı' :{self.age})" 

    @property
    # Property decorator = Read-Only Attribute
    def kimlik(self):
        return self.__kimlik #kimlik dışarıdan değiştirilemez
    
    @kimlik.setter
    def kimlik(self,kimlik):
        self.__kimlik = kimlik
        


class Child(Parent):
    def __init__(self,name,age,kimlik):
        super().__init__(name,age,kimlik)
        self.age = age
        borc = 2000

p1 = Parent("taha",25,125,5500,)
p2 = Parent("ayşe",25,126,6000)
p3 = Child("ali",15,127)

print(Parent.__dict__) #__dict__ sınıf/nesne değişkenlerini dict olarak bize verir
print(p1.__dict__)

#nesneleri ve değişkenlerini yazdıralım 
print(Parent.all)

#şuana kadar oluşturduğumuz nesnelerin isimlerini yazdıralım
for nesne in Parent.all: 
    print(nesne.name)
print("-"*40)

print(p1.kimlik)

p1.kimlik = 127 
print()


