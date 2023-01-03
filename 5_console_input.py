
input('Press enter to begin!')

# input expects only one argument
# input always returns a str
name = input('Enter your name: ')
print('Hello,',name)
print(type(name))

age = input('Hello, ' + name + ' what is your age? ')

print('Hello, ' + name + ' you are ' + age + ' years old!')