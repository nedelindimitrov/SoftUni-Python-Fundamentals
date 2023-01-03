banned_words = input().split(", ")
input_to_correct = input()

for n in range(len(banned_words)):
    current_ban = banned_words[n]

    if current_ban in input_to_correct:
        input_to_correct = input_to_correct.replace(current_ban, "*" * len(current_ban))

print(input_to_correct)
