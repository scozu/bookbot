from stats import get_num_words

# take filepath to book as input, read it, and return the contents as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# Main function that reads the book text from a file, analyzes it using stats functions,
# and outputs the results to the console
def main():
    # get the contents of the book
    book_text = get_book_text("books/frankenstein.txt")
    # count the number of words using `get_num_words` from `stats.py`
    num_words = get_num_words(book_text)
    # print result
    print(f"{num_words} words found in the document")

main()