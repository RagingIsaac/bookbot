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
