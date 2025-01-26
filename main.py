def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_instances = get_character_instances(text)
    for instance in char_instances:
        if instance.isalpha():
            print(f"The '{instance}' character was found {char_instances[instance]} times")
        


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_instances(text):
    dict = {}
    text = text.lower()
    for letter in text:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict


main()
