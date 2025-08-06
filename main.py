from stats import get_book_text
from stats import word_count
from stats import number_of_characters
from stats import sort_characters
from stats import print_report

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    letter_count = number_of_characters(book_text)
    sorted_list = sort_characters(letter_count)
    print_report(book_path, num_words, sorted_list)

main()
