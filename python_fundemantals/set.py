# Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. 
# Basic uses include membership testing and eliminating duplicate entries. 
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # fast membership testing

'crabgrass' in basket

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')

c = a - b                              # letters in a but not in b          
print(c) 

c = a | b                              # letters in a or b or both
print(c) 

c = a & b                              # letters in both a and b
print(c) 

c = a ^ b                              # letters in a or b but not both
print(c) 
                                       