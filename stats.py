def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    catalog = {}
    for char in text:
        lowered =  char.lowered()
        if lowered in catalog:
            catalog[lowered] =+ 1
        else:
            catalog[char]= 1
        return catalog

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars    



