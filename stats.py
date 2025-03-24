# accept the contents of the book as a string and return the number of words
def get_num_words(book_text):
    # return a list of words in the `book_text` string
    words = book_text.split()
    # count words in list
    num_words = len(words)
    return num_words