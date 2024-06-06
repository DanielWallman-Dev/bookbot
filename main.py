def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_book_words(book_text)
    num_characters = get_book_num_characters(book_text)
    dict_sorted_list = convert_dict_to_list(num_characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the book")
    print()

    for item in dict_sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_words(text):
    words = len(text.split())
    return words

#def get_book_num_characters(text):
    lowered_text = text.lower()
    characters = {}
    for chars in lowered_text:
        if chars in characters:
            characters[chars] += 1
        else:
            characters[chars] = 1
    return characters

#def get_book_num_characters(text):
    lowered_text = text.lower()
    characters = {}
    for chars in lowered_text:
        if (chars.isalpha() or chars.isnumeric()):
            if chars in characters:
                characters[chars] += 1
            else:
                characters[chars] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(dict):
    sorted_dict_List = []
    for char in dict:
        sorted_dict_List.append({"char": char, "num": dict[char]})
    sorted_dict_List.sort(reverse=True, key=sort_on)
    return sorted_dict_List

def get_book_num_characters(text):
    lowered_text = text.lower()
    characters = {}
    for chars in lowered_text:
        if (chars.isalpha()):
            if chars in characters:
                characters[chars] += 1
            else:
                characters[chars] = 1
    return characters

main()