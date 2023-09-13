FILE_NAME = "DATA/words.txt"
MIN_WORD_LENGTH = 10

long_word_count = 0
total_word_count = 0
with open(FILE_NAME) as words_in:
    for raw_word in words_in:
        word = raw_word.rstrip()
        if len(word) > MIN_WORD_LENGTH:
            long_word_count += 1
        total_word_count += 1

pct = round((long_word_count / total_word_count) * 100, 0)
print(f"{long_word_count} words out of {total_word_count} have a length greater than {MIN_WORD_LENGTH} ({pct}%)")
