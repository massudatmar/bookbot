from stats import get_word_count
from stats import get_character_count
from stats import sort_dictionary
from stats import sort_on
import sys 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("==================== BOOKBOT =======================")
    book_text = get_book_text(sys.argv[1])
    # print(book_text)
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------------- Word Count ------------------------")
    print(get_word_count(book_text))
    print("----------------- Character Count ------------------")
    my_dict = sort_dictionary(get_character_count(book_text))
    for dict in my_dict:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("==================== END ===========================")

main()


