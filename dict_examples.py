d1 = dict()   # empty dict
d2 = {'NC': 'Raleigh', 'PA': 'Harrisburg', 'NY': 'Albany'}
d3 = {}   # empty dict
items = [('foo', 5), ('bar', 3), ('blah', 8), ('splat', 9)]
d4 = dict(items)
d5 = dict(apple='red', banana='yellow', fig="brown")

d1["NC"] = "Raleigh"
d1["CA"] = "Sacramento"
d1["WY"] = "Laramie"
print(f"d1: {d1}")

print(f"d1['CA']: {d1['CA']}")
print(f"d1['WY']: {d1['WY']}")

# print(f"d1['PA']: {d1['PA']}")
print(f"d1.get('PA'): {d1.get('PA')}")
print(f"d1.get('PA', 'NO SUCH KEY'): {d1.get('PA', 'NO SUCH KEY')}")
print(f"d1.get('PA', 0): {d1.get('PA', 0)}")

print(f"d1.setdefault('PA', 'Harrisburg'): {d1.setdefault('PA', 'Harrisburg')}")

print(f"d1: {d1}")
print()

for state, capital in d1.items():
    print(state, capital)
print()
print(f"d1.items(): {d1.items()}")
print(f"d1.keys(): {d1.keys()}")
print(f"d1.values(): {d1.values()}")

d1['WY'] = 'Cheyenne'

print(f"d1: {d1}")

foo = {}
foo['red'] = 1
foo['red'] += 1   #  foo['red'] = foo['red'] + 1
foo['red'] += 1
foo['blue'] = 1
foo['blue'] += 1
print(f"foo: {foo}")











