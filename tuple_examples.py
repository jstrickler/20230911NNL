
person = "Bill", 'Gates', 'Microsoft', '1955-10-28'   # tuple

print(f"person[0]: {person[0]}")
print(f"person[3]: {person[3]}")
print(f"person[-1]: {person[-1]}")

# person[0], person[1], ...
first_name, last_name, product, dob = person
print(first_name, last_name)


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
print(f"people[0]: {people[0]}")
print(f"people[0][0]: {people[0][0]}")
print(f"people[0][0][0]: {people[0][0][0]}")
print()

for first_name, last_name, product, dob  in people:
    print(first_name, last_name)
print()


# for var1, var2, ... in nested_data:
#     ...

data = [
    ('a', 'b', 'd'),
    ('d', 'e'),
    ('f', 'g', 'h'),
    ('i', 'j', 'k', 'l', 'm'),
]

for x, y, *z in data:
    print(x, y, z)
print()
