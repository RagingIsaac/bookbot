# function that reads through a text file
def get_book_text(book_path):
    try:
        with open(book_path) as f:
            file_contents = f.read()
            return file_contents
    except Exception as e:
        return None

# function that counts the words of the given text
def word_count(words):
    count = words.split()
    return len(count)

# function that returns the number of times each character is in the given text
def number_of_characters(text):
    letters = {}

    for i in text.lower():
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters

def sort_characters(letters):
    letter_list = list()
    for char, count in letters.items():
        letters_dict = {"char": char, "num": count}
        letter_list.append(letters_dict)
    def sort_on(items):
        return items["num"]
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
