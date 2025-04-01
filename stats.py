# accept the contents of the book as a string and return the number of words
def get_num_words(book_text):
    # return a list of words in the `book_text` string
    words = book_text.split()
    # count words in list
    num_words = len(words)
    return num_words

# accepts string book text and returns character counts
def count_characters(book_text):
    char_count = {}
    
    for characters in book_text:
        characters = characters.lower()
        if characters in char_count:
            char_count[characters] += 1
        else: char_count[characters] = 1
        # print(char_count)
    return char_count
