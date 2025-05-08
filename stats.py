def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_by_num(dict):
    return dict["num"]

def dict_to_sorted_list(dict):
    sorted = []
    for char, count in dict.items():
        sorted.append({"char": char, "num": count})
    sorted.sort(reverse = True, key = sort_by_num)
    return sorted
