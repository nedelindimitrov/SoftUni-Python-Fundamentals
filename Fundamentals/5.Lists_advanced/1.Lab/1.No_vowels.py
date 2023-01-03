full_list = list(input())
new_list = [x for x in full_list if x != "a" and x != "o" and x != "u" and x != "e" and x != "i"]
final_answer = "".join(new_list)
print(final_answer)
