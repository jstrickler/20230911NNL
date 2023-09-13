fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

for fruit in 'apple', 'durian', 'mangosteen', 'lemon':
    print(f"fruit in fruits: {fruit in fruits}")
print()

a = "123"
b = "456"
print(f"a + b: {a + b}")

x = [1, 2, 3]
y = ['a', 'b', 'c', 'd']
print(f"x + y: {x + y}")

print(f"x * 3: {x * 3}")
flags = [0] * 10
print(f"flags: {flags}")
print('-' * 60)

nums = [800,80,1000,32,255,400,5,5000]

print(f"len(fruits), len(nums): {len(fruits), len(nums)}")
print(f"min(fruits), min(nums): {min(fruits), min(nums)}")
print(f"max(fruits), max(nums): {max(fruits), max(nums)}")
print(f"sum(nums): {sum(nums)}")
print()
print(sorted(fruits))
print()
print(sorted(nums))
print()


print(f"fruits: {fruits}")

rfruits = reversed(fruits)
print(f"rfruits: {rfruits}")


for fruit in rfruits:
    print(fruit, end=" ")
print("\n")

r = ['a', 'b', 'c']
s = ['Fred', 'Mary', 'Izzie']

for x in zip(r, s):
    print(x)
print()

zz = zip(r, s)
print(f"zz: {zz}\n")

stooges = ['Larry', 'Moe', 'Curly', 'Shemp', 'Curly Joe']
for stooge in stooges:
    print(stooge)
print()

for i, stooge in enumerate(stooges):
    if i < 3:
        print("Original:", end=" ")
    else:
        print("Other:", end=' ')
    print(stooge)
print()
print(list(enumerate(stooges)))
print()

for i in range(10):
    print(i)
print()

# range(stop)   range(start, stop)    range(start, stop, step)


print(list(range(1, 11)))
print(f"list(range(5, 101, 5)): {list(range(5, 101, 5))}")

for i in range(3):
    print("Python is the best!")






