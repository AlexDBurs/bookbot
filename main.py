from stats import *
import sys

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

# Función para extraer el texto
def get_book_text(path_to_file=sys.argv[1]):

    with open(path_to_file, encoding="utf8") as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text()
    word_count = word_counter(file_contents)
    letter_dict = letter_counter(file_contents)
    letter_dict_list = dict_sorter(letter_dict)

    print(f"{word_count} words found in the document")
    print(
        """============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found 75767 total words
    --------- Character Count -------"""
    )

    for dict1 in letter_dict_list:
        print(f"{dict1['name']}: {dict1['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
