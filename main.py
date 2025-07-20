from stats import get_book_text
from stats import word_count
from stats import number_of_characters

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    letter_count = number_of_characters(book_text)
    print(letter_count)

main()
