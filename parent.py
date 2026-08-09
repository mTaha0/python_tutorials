class Parent:
    #sınıf değişkenleri
    borc = 1000
    kredi = 2000

    all = [] # oluşturulan nesneleri eklemek için liste oluşturduk 
    
    def __init__(self,name,age,money=5000, kimlik=int):

        #argümanları kontrol edelim
        assert money >= 5000, f"Para {money}'den büyük olmalıdır"
        assert age >= 0
        assert kimlik == int, "kimlik sayı olmalıdır"

        #nesne değişkenleri
        self.name = name
        self.age = age
        self.money = money
        self.kredi = Parent.kredi # burada nesneye bağımsız bir kredi atamış olduk
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