def count_words(string):
    words = string.split()
    # print(words)
    num_words = len(words)
    # print(num_words)
    return num_words


if __name__ == "__main__":
    # count_words("this is a string")
    # count_words("This is another string with some other words")
    with open("book.txt", encoding="utf8") as f:
        text = f.read()
        num_chars = len(text)
        num_words = count_words(text)
        print(f"The text has {num_chars} characters, and {num_words} words.")
