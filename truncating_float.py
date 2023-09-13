x = 39.329833

print(f"{x:.2f}")

print(f"{str(x).split('.')[0]}.{str(x).split('.')[1][:2]}")

a, b = str(x).split('.')
print(f"{a}.{b[:2]}")
