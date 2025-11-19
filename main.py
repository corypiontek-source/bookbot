from stats import get_num_words, get_num_chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    char_freq = get_num_chars(text)

    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print(char_freq)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()