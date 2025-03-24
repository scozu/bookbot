# accept the contents of the book as a string and return the number of words
def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words