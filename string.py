text = "Merhaba"

#use \' to escape the single quote...
print("Taha\'s pencil is black") #Taha's pencil is black

print("\"Merhaba\"dedi") #"Merhaba"dedi

s = 'First line.\nSecond line.'  # \n means newline
print(s)

print(r'C:\this\name')  # note the r before the quote

print("""\
    Merhaba""") #\ çıktının en başında boş satır olmasını engeller


#Strings can be concatenated (glued together) with the + operator, and repeated with *:
print(3 *( "um" + "un")) #umunumunumun

print('Py' 'thon') #Python
#This feature is particularly useful when you want to break long strings:
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

word = 'Python'
print(word[0]) #P

word[-1]  # last character
word[0:2] #Py 2 dahil değil                  
word[:2]  
word[-2:] #on

word[:2] + word[2:] #Python               

len(word) #6

#*string methods
print("PYTHON".lower())
print("PYTHON".upper())
print("merhaba".capitalize())
print("Merhaba".casefold())
print('Python'.center(10, '-'))

print("   merhaba   ".strip())
print("***merhaba***".lstrip('*'))
print("***merhaba***".rstrip('*'))

print("Merhaba,ben,taha".split(','))
print('-'.join(["Merhaba", "Ben", "Taha"]))
print('Merhaba ben Taha'.replace("Taha", "Ahmet"))
print("Merhaba ben taha".find("taha"))
print("elma aldım elma".count('elma'))

print("Merhaba".startswith('Merhaba'))
print("filname.png".endswith('.png'))