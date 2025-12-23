def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    wordcount = len(words)
    print(f"Found {wordcount} total words")
    


get_num_words()
