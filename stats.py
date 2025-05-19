def get_num_words(text):
    word_list = text.split()
    return len(word_list)

word_count = get_num_words(book_text)  # This gives global access to Word Count.
print(f"{word_count} words found in the document")