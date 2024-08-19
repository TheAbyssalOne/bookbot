def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words(text)
    list_count_chars = count_chars(text)
    sort_lists(list_count_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(list_words):
    wrds = list_words.split()
    count = 0
    for x in wrds:
        count += 1
    print(f"{count} words found in document")

def count_chars(book):
    char_dict = {}          # Initialize the dictionary to store character counts
    list_chars = book.lower()  # Convert the text to lowercase
    allowed_chars = set("abcdefghijklmnopqrstuvwxyz")
    for char1 in list_chars:
        if char1 in allowed_chars:
            if char1 in char_dict:
                char_dict[char1] += 1
            else:
                char_dict[char1] = 1
    return char_dict

def sort_lists(unsorted_dict):
    new_list = []
    for char, count in unsorted_dict.items():
        new_list.append([char,count])
    new_list.sort(key=lambda x:x[1], reverse=True)
    total_value = 0
    for char, count in new_list:
        total_value += count
    print(f"{total_value} characters found in the document")
    for char, count in new_list:
        print(f"The {char} character was found {count} times")
main()