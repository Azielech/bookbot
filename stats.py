def get_num_words(text):
    word_list = text.split()
    return len(word_list)


def get_num_char(text):
    word_list = text.lower()
    counts = {}

    for char in word_list:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

def get_book_report(book_data): 
    dictionaries = []

    for char, num in book_data.items():
        new_dict = {"char": char, "num": num}  # Create a new dictionary
        dictionaries.append(new_dict)  # Append the dictionary to the list
        dictionaries.sort(reverse=True, key=sort_report)
    return dictionaries

def sort_report(dict):
    return dict["num"]