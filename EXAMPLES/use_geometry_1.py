import alpha.mathlib.geometry  #  load and execute alpha/mathlib/geometry.py
import sys

a1 = alpha.mathlib.geometry.circle_area(8)
a2 = alpha.mathlib.geometry.rectangle_area(10, 12)
a3 = alpha.mathlib.geometry.square_area(7.9)
print(a1, a2, a3)

# module search order
#  1. current folder
#  2. folders in PYTHONPATH
#  3. builtin folders under sys.prefix
print(f"sys.prefix: {sys.prefix}\n")
for path in sys.path:
    print(path)
print()

sys.path.insert(0, "my_folder")
print(alpha.mathlib.geometry.get_module_name())
