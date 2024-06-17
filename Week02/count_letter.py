def count_chars(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


if __name__ == "__main__":
    word = "Happiness"
    print(count_chars(word))
    word2 = "Python is fun"
    print(count_chars(word2))
