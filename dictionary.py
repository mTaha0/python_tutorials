dictionary = {"anahtar": "kilit", "tür": "insan"}
dictionary['isim'] = 'emin'
print(dictionary)

print(dictionary["anahtar"]) #kilit 
list(dictionary)
print(list(dictionary))
print(sorted(dictionary))

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

new_dict = {x: x**2 for x in (2, 4, 6)}
print(new_dict)
print(dict(sape=4139, guido=4127, jack=4098))

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)