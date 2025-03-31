import sys
from stats import (
    get_num_words,
    count_characters,
    sort_character_counts,
)

def main():
    #"books/frankenstein.txt"
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    chars_dict = count_characters(text)
    chars_sorted_list = sort_character_counts(chars_dict)
    #print(sys.argv)
    print_report(filepath, num_words, chars_sorted_list)

def get_book_text(filepath: str):
    contents = "Filepath does not exist"
    with open(filepath) as b:
        contents = b.read()

    return contents

def print_report(filepath, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if item['key'].isalpha():
            print(f"{item['key']}: {item['value']}")

main()
