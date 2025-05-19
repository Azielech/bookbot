def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

book_text = get_book_text("books/frankenstein.txt") # This give global access to the Book Text.
print(book_text)

from stats import get_num_words