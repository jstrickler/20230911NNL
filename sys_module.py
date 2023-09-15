import sys   # info about the current script
import dataclasses


print(f"sys.argv: {sys.argv}")
print(f"dir(sys): {dir(sys)}")
print('-' * 60)
print(f"sys.prefix: {sys.prefix}")
print(f"sys.executable: {sys.executable}")
print(f"sys.version_info: {sys.version_info}")
print(f"sys.version: {sys.version}")
print(f"sys.platform: {sys.platform}")  #  win32  darwin linux
print()

print(f"sys.modules['dataclasses']: {sys.modules['dataclasses']}")
print()
print(sys.modules.keys())
print()

elements = 10000
nlist = list([123] * elements)
ntuple = tuple((123,) * elements)

print(f"sys.getsizeof(nlist): {sys.getsizeof(nlist)}")
print(f"sys.getsizeof(ntuple): {sys.getsizeof(ntuple)}")
print()


print("Hello. The sea is calm")
print("OMG! The sea is raging and we're doomed!", file=sys.stderr)








