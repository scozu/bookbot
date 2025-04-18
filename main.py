import sys
from stats import get_num_words, count_characters, sort_dict

# take filepath to book as input, read it, and return the contents as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
        
    return book_text
    
def print_report(path, word_count, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # loop through sorted dictionary to print characters and their counts
    for char_dicts in sorted_characters:
        char = char_dicts["char"]
        count = char_dicts["count"]
        # skip over non-alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

# Main function that reads the book text from a file, analyzes it 
# using stats functions, and outputs the results to the console
def main():
    # path = "books/frankenstein.txt"
    # use sys.argv to accept book text paths
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = get_num_words(book_text)
    # character_count = count_characters(book_text)
    sorted_characters = sort_dict(book_text)
    
    print_report(path, word_count, sorted_characters)

main()