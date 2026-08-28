# Though tuples may seem similar to lists, they are often used in different situations and for different purposes. 
# Tuples are immutable, and usually contain a heterogeneous sequence of elements 
# that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). 
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

t = 12345, 54321, 'hello!'
t[0]
print(type(t))

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u) #((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v[0][1] = 5
print(v)

x, y, z = t
print(x,y,z) 

singleton = 'hello',    # <-- note trailing comma
print(type(singleton))