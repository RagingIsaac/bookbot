def get_book_text(book_path):
    try:
        with open(book_path) as f:
            file_contents = f.read()
            return file_contents
    except Exception as e:
        return None

def word_count(words):
    num_words = get_book_text("books/frankenstein.txt")
    count = num_words.split()
    return len(count)

