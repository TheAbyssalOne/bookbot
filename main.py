def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    count_words(text)
    count_chars(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(list_words):
    wrds = list_words.split()
    count = 0
    for x in wrds:
        count += 1
    print(count)

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
    print(char_dict)

main()