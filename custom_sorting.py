fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f0 = sorted(fruits)
print(f"f0: {f0}\n")

# str.lower

f1 = sorted(fruits, key=str.lower)
print(f"f1: {f1}\n")

f2 = sorted(fruits, key=len)
print(f"f2: {f2}\n")

def len_and_name(fruit):
    comparison_value = len(fruit), fruit.lower()
    print(f"comparing {fruit} as {comparison_value}")
    return comparison_value

f3 = sorted(fruits, key=len_and_name)
print(f"f3: {f3}\n")

def last_letter(s):
    return s[-1]

f4 = sorted(fruits, key=last_letter)
print(f"f4: {f4}\n")

f5 = sorted(fruits, key=lambda f: f[-1])
print(f"f5: {f5}\n")

# lambda params:return-value

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(p):
    return p[1], p[0]

p1 = sorted(people, key=by_dob)
for person in p1:
    print(person)
print()

for person in sorted(people, key=lambda p: (p[1], p[0])):
    print(person)
print()

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

for code, name in sorted(airports.items()):
    print(code, name)
print()

for code, name in sorted(airports.items(), key=lambda a: (a[1], a[0])):
    print(code, name)
print()

f6 = sorted(fruits, key=str.lower, reverse=True)
print(f"f6: {f6}\n")

fruits.sort(key=str.lower)
print(f"fruits: {fruits}\n")








