#Fibonacci series:
# the sum of two elements defines the next
a , b = 0, 1
while a < 10:
    print(a)
    a , b = b, a + b


#if
x = 5
if x > 6:
    print("x  is greater than 65")
elif x < 3:
    print("x is lower than 3")
else:
    print("idk the value of x")

#for 
liste = ["a","b","c","d"]
for _ in liste:
    print(_)

a = 0
for a in range(20):
    print(a)



#match
point = (0,1)
match point:
    case (0,0):
        print("origin")
    case (0,1):
        print(f"x is {point[0]} y is {point[1]}")
