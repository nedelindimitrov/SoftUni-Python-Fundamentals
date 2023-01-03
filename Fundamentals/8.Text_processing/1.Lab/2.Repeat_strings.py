words_input = input().split(" ")
final_output = ""

for n in range(len(words_input)):
    current_word = words_input[n]
    final_output += current_word * len(current_word)

print(final_output)
