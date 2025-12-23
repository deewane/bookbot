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
    
def samewords():
    text = get_book_text("books/frankenstein.txt")
    word_to_find = input("type in the word you want to find")
    words = text.split()
    num_word = 0
    for word in words:
        if word == word_to_find:
            num_word += 1
    if num_word == 0:
        print("word not found")
    else:
        print(f"the word {word_to_find} was found a number of {num_word}")


samewords()
