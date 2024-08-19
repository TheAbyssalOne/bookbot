def main():
    book_path = "books/frankenstein.txt"  # Path to the text file
    text = get_book_text(book_path)       # Read the content of the file
    count_words(text)                     # Count and print the number of words
    list_count_chars = count_chars(text)  # Count the occurrences of each character
    sort_lists(list_count_chars)          # Sort and print the character frequency

def get_book_text(path):
    with open(path) as f:                 # Open the file
        return f.read()                   # Return its content as a string

def count_words(list_words):
    wrds = list_words.split()             # Split the text into words
    count = 0
    for x in wrds:                        
        count += 1                        # Count each word
    print(f"{count} words found in document")  # Print the total word count

def count_chars(book):
    char_dict = {}                        # Initialize dictionary for character counts
    list_chars = book.lower()             # Convert text to lowercase
    allowed_chars = set("abcdefghijklmnopqrstuvwxyz")  # Define valid characters
    for char1 in list_chars:              # Iterate over each character in the text
        if char1 in allowed_chars:        # Consider only valid characters
            if char1 in char_dict:
                char_dict[char1] += 1     # Increment character count
            else:
                char_dict[char1] = 1      # Initialize character count
    return char_dict                      # Return dictionary of character counts

def sort_lists(unsorted_dict):
    new_list = []                         # Initialize list for sorted characters
    for char, count in unsorted_dict.items():
        new_list.append([char, count])    # Convert dictionary to list of lists
    new_list.sort(key=lambda x: x[1], reverse=True)  # Sort by count in descending order
    total_value = 0
    for char, count in new_list:
        total_value += count              # Calculate total character count
    print(f"{total_value} characters found in the document")  # Print total character count
    for char, count in new_list:
        print(f"The {char} character was found {count} times")  # Print character frequencies

main()