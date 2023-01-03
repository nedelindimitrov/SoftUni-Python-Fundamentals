word = input()

while word != "End":
    new_word = ""
    if word == "SoftUni":
        pass
    else:
        for char in word:
            new_word = new_word + 2 * char
        print(new_word)
    word = input()
