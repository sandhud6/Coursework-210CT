def deleteVowels (word):
    vowels = ["a","u", "e", "i"]
    words = []

    for i in word:
        if i.lower() not in vowels:
            words.append(i)

    return "".join(words)
