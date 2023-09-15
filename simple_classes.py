
colors = list()   #  creating an instance of the list class     list.__init__(...)
colors.append('pink')    # list.append(colors, 'pink')
colors.append('maroon')
colors.append('red')
colors.append('scarlet')

print(f"colors.index('red'): {colors.index('red')}")

x = 5398954382
print(f"type(x): {type(x)}")
print(f"dir(x): {dir(x)}")
print(f"x.bit_length(): {x.bit_length()}")

class Dog:  # inherits from 'object'
    def bark(self):
        print("Woof! Woof!")

d = Dog()
d.bark()    #   Dog.bark(d)

d2 = Dog()
d3 = Dog()

print(f"dir(d): {dir(d)}")
