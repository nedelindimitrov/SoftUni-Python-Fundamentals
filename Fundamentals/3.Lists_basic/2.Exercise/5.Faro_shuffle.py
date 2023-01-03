first_input = input().split(" ")
old_list = list(first_input)
shuffle_rounds = int(input())
new_list = list()
all_cards = int(len(old_list))
half_cards = int(all_cards / 2)

for _ in range(shuffle_rounds):

    for x in range(half_cards):
        for y in range(x, all_cards , half_cards):
            new_add = str(old_list[y])
            new_list.append(new_add)

    old_list = list(new_list)
    new_list.clear()

print(old_list)
