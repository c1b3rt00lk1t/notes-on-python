
name = input("Name: ")
condition1 = name == 'John'
condition2 = name == 'Andrea'
if condition1:
    print('Your name is John')
    print('Congratulations!')
elif condition2:
    print('Your name is Andrea')
    print('Very well!')
else:
    print('Bad luck...')

print('Finished!')

x = 5

# In-line if statement
result = "Ok" if x > 5 else "Not ok"

print(result)