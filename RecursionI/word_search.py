words = ['hello', 'world', 'how', 'are', 'you', 'recurring']

def find_word(find):
    for word in words:
        if word == find:
            return word

    return None

def find_word_recurring(find, index):
    # base case 1
    if index <= -1:
        return None

    # base case 2
    if words[index] == find:
        return words[index]

    # recursive case
    return find_word_recurring(find, index - 1)

if __name__ == "__main__":
    print(find_word('recurring'))
    print(find_word_recurring('recurring', len(words) - 1))