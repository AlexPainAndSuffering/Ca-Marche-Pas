def filter_words(string, whitelist):
    filtered_words = []
    for word in string:
        if word in whitelist:
            filtered_words.append(word)
    return filtered_words

def word_exist(string, whitelist):
    for word in whitelist:
        if word in string:
            return True
    return False