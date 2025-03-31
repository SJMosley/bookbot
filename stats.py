
def get_num_words(book_text: str):
    return len(book_text.split())

def count_characters(book_text: str):
    char_counts = {}
    char_list = list(book_text.lower())

    for char in char_list:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
def sort_on(dict):
    #print(dict["value"])
    return dict["value"]

def sort_character_counts(char_counts):
    sorted_list = []
    for key in char_counts:
        sorted_list.append({"key": key, "value":char_counts[key]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
