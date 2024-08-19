def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    count_words(text)
    # print(count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(list_words):
    wrds = list_words.split()
    count = 0
    for x in wrds:
        count += 1
    print(count)

main()
