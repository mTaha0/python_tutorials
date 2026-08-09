def fib(n):
    """Print a Fibonacci series less than n."""

    a, b = 0, 1

    while a < n :
        print(a, end= " ")
        a , b = b, a + b

fib(200)

#default argumant 

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#bu fonksiyonda promt zorunlu argümandır, diğer ikisi isteğe bağlı argümanlardır
#fonksiyonu çağırırken sadece zorunluyu kullanmak yeterlidir, kalanı kullanmasak da sorun
#yaşanmaz

print("_"*40)
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print(voltage, state, action, type)

parrot(1000, state= " soft")

#argüman ismini kullanarak sıraya göre değil istediğimiz 
#argümana göre atama yapabiliriz
def order(kind, *arguments, **keywords):
    print(f"elinizde {kind} var mı ?")
    print(f"üzgünüm elimizdeki bütün {kind} bitti")
    for arg in arguments:
        print(arg)
    print("_"*40)
    for kw in keywords:
        print(kw)

order("ezine peyniri ",
     "kars kaşarı","tulum peyniri",
      satici="ahmet", yer="artvin") 


def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass
# / öncesi argümanlar sadece pozisyonel,
# / ile * arasındakiler hem pozisyonel hem de anahtarlı
# * sonrasındakiler de sadece anahtarla çalışan argümanlardır


liste = [0,2,3,7]

for x in liste:
    print(x)

a = 25 

