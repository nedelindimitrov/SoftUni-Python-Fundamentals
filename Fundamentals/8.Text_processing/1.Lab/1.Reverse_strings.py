word = input()

while word != "end":
    new_word = reversed(word)
    reversed_word = "".join(new_word)
    print(f"{word} = {reversed_word}")
    word = input()
