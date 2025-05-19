def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

book_text = get_book_text("books/frankenstein.txt") # This give global access to the Book Text.
print(book_text)

from stats import get_num_words #This give access to the num_words functon inside of main.
word_count = get_num_words(book_text)
print(f"{word_count} words found in the document")