from pprint import pprint

FILE_NAME = "../DATA/knights.txt"

def main():
    data = read_file()
    pretty_print_info(data)
    print()
    print_titles(data)
    print()
    print(get_field(data, 'Robin', 2))

def read_file():
    info = {}  # create empty dict

    with open(FILE_NAME) as knights_in:
        for line in knights_in:
            name, title, color, quest, comment = line.rstrip('\n\r').split(":")
            info[name] = title, color, quest, comment  # create new dict element with name as key and a tuple of the other fields as the value
    return info

def pretty_print_info(knight_info):
    pprint(knight_info)

def print_titles(knight_info):
    for name, info in knight_info.items():
        print(info[0], name)

def get_field(knight_info, knight_name, field_index):
    return knight_info[knight_name][field_index]


main()