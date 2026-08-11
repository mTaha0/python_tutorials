import numpy as np

rng = np.random.default_rng()
rng= np.random.default_rng(seed=1) #seed, aynı sayıları tekrar üretmeyi sağlar

#random float
print(rng.random())

#random integer: integers(low=value1, high=value2, size=array_size)
print(rng.integers(low=1, high=15))
print(rng.integers(low=5 ,high=10, size=1))

#gelme olasılığı eşit ondalıklı sayı üretimi
print(np.random.uniform(low=7, high=15))
print(np.random.uniform(low=-3, high=15,size=(3,3)))

#seed çağrıldıktan sonra ondan sonraki değişkenler seed değerleri aynı ise o seed'e göre sayı üretir
np.random.seed(seed=1)
print(np.random.uniform(low=1, high=15, size=(3, 2)))

#array-shuffle
rng2 = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng2.shuffle(array)
print(array)

fruits = np.array(["elma","armut","karpuz","vişne"])
fruit = rng2.choice(fruits)
print(fruit)

fruits = rng2.choice(fruits, size=(3,3))
print(fruits)

emoji = np.array(["🫡", "😂", "🤣", "💕", "😘", "👌", "😒", "😍", "❤️"])
emoji = rng2.choice(emoji, size=(3,3))
print(emoji)
