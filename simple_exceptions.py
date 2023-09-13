
FILE_NAME = "DATA/wombats.txt"

try:
    with open(FILE_NAME) as wombats_in:
        pass
except FileNotFoundError as err:
    print(err)

print("ALL DONE")