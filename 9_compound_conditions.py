x = 1
y = 4

compound = not(x and y < x + 5) or True
print(compound)

print( True == (not False))

# operator precedence:
# parenthesis
# conditional/comparision operators go first
# not
# and
# or