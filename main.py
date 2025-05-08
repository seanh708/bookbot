from stats import get_word_count, get_char_count, dict_to_sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    sorted_chars = []

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_of_words = get_word_count(text)
    char_counts = get_char_count(text)
    sorted_chars = dict_to_sorted_list(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    print_alpha_chars_by_count(sorted_chars)
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_alpha_chars_by_count(char_list):
    for item in char_list:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['num']}")


main()