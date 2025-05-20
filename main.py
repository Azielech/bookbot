import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):   
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

file_path = sys.argv[1] #This gives access to the file path for the report generator.

book_text = get_book_text(sys.argv[1]) # This give global access to the Book Text.
#print(book_text) 
#^ --------------Release for debugging

from stats import get_num_words #This give access to the num_words functon inside of stats.
word_count = get_num_words(book_text)
#print(f"{word_count} words found in the document")
#^ --------------Release for debugging

from stats import get_num_char #This gives access to the num_char function inside of stats.
char_count = get_num_char(book_text)
#print(f"{char_count}")
#^ --------------Release for debugging

from stats import get_book_report
sorted_report = get_book_report(char_count)
#print(sorted_report)
#^ --------------Release for debugging

#Report generation
print("============ BOOKBOT ============")
print(f"Analyzing book found at {file_path}...")  
print("----------- Word Count ----------")
print(f"Found {word_count} total words")  
print("--------- Character Count -------")
for report_data in sorted_report:
    sorted_char = report_data["char"]
    sorted_num = report_data["num"]
    if sorted_char.isalpha():
      print(f"{sorted_char}: {sorted_num}")
print("============= END ===============")