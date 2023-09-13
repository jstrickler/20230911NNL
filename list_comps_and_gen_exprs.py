fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    expr = f.upper()
    # if ...
    f0.append(expr)
print(f"f0: {f0}\n")

f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

#  [expr for var in iterable]
#  [expr for var in iterable if condition]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

f3 = [f.title() for f in fruits if len(f) < 6]
print(f"f3: {f3}\n")

f4 = [f for f in fruits if len(f) > 8]
print(f"f4: {f4}\n")

values = [8, 'abc', 12, 15.9, 45, None, 'wombat', 0, -6]

numeric_values = [x for x in values if isinstance(x, (int, float))]
print(f"numeric_values: {numeric_values}\n")

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 
        'spam', 'spam', 'spam', 'spam', 'eggs', 'eggs', 'toast', 'spam', 
        'spam', 'spam', 'tofu', 'lamb kidneys', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam']

good_foods = [(f.title() if len(f) < 5 else f.upper()) for f in food if f != 'spam' if 'kidneys' not in f]
print(f"good_foods: {good_foods}\n")

#   A if B else C

good_foods_gen = (f for f in food if f != 'spam' if 'kidneys' not in f)
print(f"good_foods_gen: {good_foods_gen}\n")

upper_fruits_gen = (f.upper() for f in fruits)
for fruit in upper_fruits_gen:
    print(fruit)
