import random
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# "┌─────────┐"
# "│         │"
# "│    ●    │"
# "│         │"
# "└─────────┘"

dice_art={
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}
total=0
dice=[]

num_of_rolls=int(input("enter the number of rolls: "))
for die in range(num_of_rolls):
    dice.append(random.randint(1,6))

# for die in range(num_of_rolls):
#     for line in dice_art.get(dice[die]):
#         print(line)

for line in range (5):
    for die in dice:
        print(dice_art.get(die)[line],end=" ")
    print()

# for die in range(num_of_rolls):
#     for line in dice_art.get(dice[die]):
#         print(line)

# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line],end="")
#     print()

for die in dice:
    total+=die
print(f"Total: {total}")