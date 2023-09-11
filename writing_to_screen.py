
person = "Bart Simpson"
city = "Springfield"
value = 38.469398393

print(person, city, value)   # str(person) + ' ' + str(city) + ' ' + str(value) + '\n'

print(person, city, value, sep="//")
print(person, city, value, sep="")
print(person)  # '\n'
print(city)  # '\n'
print(value)  # '\n'
print()

print(person, end=',')
#if ????
print(city, end="//")
# else ???
print('other value')
print(value)

#  Bart Simpson lives in Springfield

s = f"{person} lives in {city}"
print(s)
print(f"2 + 2 is {2 + 2}")
a = 5
b = 10
print(f"{a} + {b} is {a + b}")

print(f"a: {a}")

print(f"value is {value}")
print(f"value is {value:.2f}")
print("value is {:.2f}".format(value))  # old and ...ugly (imo)
print("value is %.2f" % (value))

large_value = 395320958203958209358
print(f"{large_value:,d}")

big_value = 12_345_830

print(1_1_1_2_8_6)
