from stats import get_book_text
from stats import word_count

def main():
    num_words = word_count("words")
    print(f"{num_words} words found in the document")

main()
