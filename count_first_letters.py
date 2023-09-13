DATA_FILE = "DATA/words.txt"

counts = {}

with open(DATA_FILE) as words_in:
    for raw_line in words_in:
        first_letter = raw_line[0]
        if first_letter not in counts:
            counts[first_letter] = 0   # initialize value for this letter
        counts[first_letter] += 1  # increment count for this letter

for letter, count in counts.items():
    print(letter, count)
