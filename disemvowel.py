
disemvowel(word):
    vowels = "aeiouAEIOU"
    new_word = []

    for letter in word:
        if letter not in vowels:
            new_word.append(letter)

    new_word = ''.join(new_word)
    return new_word
