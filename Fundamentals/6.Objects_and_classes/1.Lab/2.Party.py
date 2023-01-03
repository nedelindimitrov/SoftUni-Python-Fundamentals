class Party():
    def __init__(self):
        self.people_list = list()


party = Party()

line = input()
while line != "End":
    party.people_list.append(line)
    line = input()

print(f"Going: {', '.join(party.people_list)}")
print(f"Total: {len(party.people_list)}")
