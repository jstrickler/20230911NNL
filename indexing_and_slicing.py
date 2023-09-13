fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"fruits[0]: {fruits[0]}")
print(f"fruits[10]: {fruits[10]}")
print(f"fruits[-1]: {fruits[-1]}")
print()

print(f"fruits[3:8]: {fruits[3:8]}")
print(f"fruits[3:5] {fruits[3:5]}")

print(f"fruits[:4]: {fruits[:4]}")
print(f"fruits[8:]: {fruits[8:]}")
print(f"fruits[:]: {fruits[:]}")

print(f"fruits[-3:]: {fruits[-3:]}")

#   LIST[-2]   same as LIST[len(LIST) - 2]
print('-' * 60)

for fruit in fruits:
    print(fruit)
print()

for fruit in fruits[:4]:
    print(fruit)
print()

for fruit in fruits:
    # fruit = fruits[0]
    # fruit = fruits[1]
    # ...
    print(fruit)
    if len(fruit) == 4:
        break
print()
print(f"fruit: {fruit}")
print()


