import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import count_words
from stats import count_characters
from stats import count_words, count_characters, sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = count_words(text)
    print(f"{word_count} words found in the document")
    char_counts = count_characters(text)
    print(char_counts)
    
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = count_words(text)
    char_counts = count_characters(text)

    sorted_chars = sort_char_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha(): 
            print(f"{char}: {count}")

main()
