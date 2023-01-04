
# When comparing ints and floats, they will evaluate to True if the value is the same

x1 = 2
x2 = 2.0

first_condition = x1 == x2
print(first_condition)

x3 = 3
x4 = 3.0

second_condition = x3 != x4
print(second_condition)

# operators include: <, >, <=, >=, 

#ord() allows to know the ascii code of a char and chr returns the character corresponding to an ASCII code
print(ord('A'), ord('a'))
print(chr(67))