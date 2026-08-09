from abc import ABC,abstractmethod

class Bildirim(ABC):
    #abstract class ve metodu oluşturduk

    @abstractmethod
    def send(self,kisi,mesaj):
        pass


class Sms(Bildirim):
    def send(self, kisi, mesaj):
        print("SMS talebi oluşturuldu...")
        print(f"SMS içeriği = >'{mesaj}'")
        print(f"{kisi.upper()} kişisine mesaj gönderiliyor")


class Email(Bildirim):
    def send(self, kisi, mesaj):
        print("Email talebi oluşturuldu...")
        print(f"email içeriği = > '{mesaj}'")
        print(f"{kisi} kişisine mesaj gönderiliyor")

class PushBildirim(Bildirim):
    def send(self, kisi, mesaj):
        print("PushBildirim talebi oluşturuldu...")
        print(f"pushbildirim içeriği = >  '{mesaj}'")
        print(f"{kisi} kişisine mesaj gönderiliyor")


def mesaj_gönder(kullanıcı_adı, bildirim_tercihi,mesaj):
    print(f"{kullanıcı_adı} isimli kişinin mesajı onaylandı")

    bildirim_tercihi.send(kullanıcı_adı,mesaj)

sms = Sms()
email = Email()
push = PushBildirim()

mesaj_gönder("taha",sms,"naber")
    


        
        
