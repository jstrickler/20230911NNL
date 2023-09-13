

def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None


say_hello()  # Call function (arguments, if any, in () )


def get_hello():
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()


def sqrt(num):  # Function takes exactly one argument
    return num ** .5


m = sqrt(1234)  # Call function with one argument
n = sqrt(2)

print("m is {:.3f} n is {:.3f}".format(m, n))


def spam():
    print("spam!")
    return

spam()

#       required positional
def eggs(var1, var2, var3):
    print(var1, var2, var3)

eggs(1, 2, 'a')
eggs('a', 5, 98)

#     optional positional
def toast(*args):
    print(args)

toast(5)
toast(5, 8, -3, 'wombat')

def ham(*, color, country):
    print(color, country)

ham(color='red', country='Burkina Faso')
ham(country="Thailand", color="blue")


def search_text(text, search_term, *, ignore_case=False):
    pass

search_text("my text", "my", ignore_case=True)






