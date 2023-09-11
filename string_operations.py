actor = "Chris Hemsworth"

print("wo" in actor)  # test for 'membership'

print("Liam and " + actor)

print(len(actor))

x = actor.upper()
print("actor:", actor)
print("x:", x)

print(actor.count('h'))  #  'Chris Hemsworth'
print(actor.lower().count('h'))

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))   # wilLIAM
#  .endswith(...)

print(actor.find('wor'))
print(actor.find('wombat'))


file_name = "spam.txt"
file_name_base = file_name.removesuffix('.txt')
print(file_name, file_name_base)
print(actor.replace('Chris', 'Liam'))

data = 'abc:def:ghi'
fields = data.split(':')
print(fields)

name = 'John Jacob Jingleheimer Schmidt'
print(name.split())

s = "     All my exes live in Texas     "
print(s + "|")
print(s.lstrip() + "|")
print(s.rstrip() + "|")
print(s.strip() + "|")
print()

raw_cost = "$1000"
cost = raw_cost.lstrip("$")
print(raw_cost, cost)





