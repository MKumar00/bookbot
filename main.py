def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    words=count_words(text)
    print(f"{words} words found in the document")
    letters = count_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(letters)
    for i in chars_sorted_list:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times")
    print("--- End Report ---")

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return(len(text.split()))

def count_letters(text):
    char_count = {}
    for i in text:
        lowered = i.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
    return char_count


main()
