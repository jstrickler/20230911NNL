fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

with open('myfruits.txt', 'w') as fruits_out:
    for fruit in sorted(f.upper() for f in fruits):
        fruits_out.write(f"{fruit}\n")

MIN_LENGTH = 20
INPUT_FILE_NAME = 'DATA/words.txt'
OUTPUT_FILE_NAME = 'long_words.txt'

with open(INPUT_FILE_NAME) as words_in:
    with open(OUTPUT_FILE_NAME, 'w') as words_out:
        for raw_word in words_in:
            word = raw_word.rstrip()
            if len(word) > MIN_LENGTH:
                words_out.write(raw_word)
