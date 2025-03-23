# take filepath to book as input and return the contents as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# use `get_book_text` to print the contents of "frankenstein"
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

main()

# accept the contents of the book as a string and return the number of words
