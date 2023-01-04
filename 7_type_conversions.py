# int(), str(), float(), bool() can be used to convert the types
x = "4"
y = int(x)
print(y + 5)
print(type(x), type(y))

z = "4.5"
w = float(z)
print(type(z), type(w))

# A float can be converted into an int (it removes the decimals) but a string representing a float cannot be directly converted to int
print(type(int(float(z))))


# The bool() conversion of an empty string or 0 is False, the conversion of a non-empty string or any other number is True
print(bool(""))
print(bool(0))
print(bool("Thasdasd"))
print(bool(8))

# Practical example
number = input("Please, enter a number: ")
result = float(number) + 8
print("The result is", result)