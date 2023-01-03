input_text = input().split(":")

for i in range(1, len(input_text)):
    current_piece = input_text[i]
    current_emoji = current_piece[0]

    print(f":{current_emoji}")
