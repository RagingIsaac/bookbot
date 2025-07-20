def get_book_text(book_path):
    try:
        with open(book_path) as f:
            file_contents = f.read()
            return file_contents
    except Exception as e:
        return None

def word_count(words):
    count = words.split()
    return len(count)

def number_of_characters(text):
    letters = {}

    for i in text.lower():
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters
