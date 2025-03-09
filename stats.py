def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    text = text.lower()
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_count(char_counts):
    def sort_on(dict_item):
        return dict_item["count"]
    
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "count": count})
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
