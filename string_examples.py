s1 = "spam\n"   #  \n \r \t \f \b ...
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''


print(s1 == s2)
print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("Guido's the ex-\"BDFL\" of Python")
print("""Guido's the ex-"BDFL" of Python""")

def doit():
    """
    Do this thing. Do it well. 
    """
    pass

query = """
select * 
from customers
where state = 'WA'
order by 'balance'
"""

s5 = r"spam\n"
print(s5)

print("It was 100\u00B0 in Durham last week")



