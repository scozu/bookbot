# accept the contents of the book as a string and return the number of words
def get_num_words(book_text):
    # return a list of words in the `book_text` string
    words = book_text.split()
    # count words in list
    num_words = len(words)
    
    # print(num_words)
    return num_words

# accept string book text and return character counts
def count_characters(book_text):
    # empty dictionary for characterc count
    char_count = {}
    
    for characters in book_text:
        characters = characters.lower()
        if characters in char_count:
            char_count[characters] += 1
        else: char_count[characters] = 1
    
    # print(char_count)
    return char_count

def sort_on(dict):
    return dict["count"]

def sort_dict(book_text):
    char_count = count_characters(book_text)
    char_sort = []
    
    # Take the dictionary of characters and their counts and 
    # return a sorted list of dictionaries.
    # Each dictionary should have two key-value pairs: 
    # one for the character itself and one for that character's count.
    
    for char, count in char_count.items():
        char_dict = {"char": char, "count": count}
        char_sort.append(char_dict)
    
    char_sort.sort(reverse=True, key=sort_on)

    # print(char_sort)
    return char_sort
    
