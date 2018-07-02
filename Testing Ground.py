import itertools
gameboard = []

user_size_choice = 5
flattened_list = []

# print(gameboard)
for i in range(0, user_size_choice):
    gameboard.append([str(i + 1)])
    gameboard[i].append([" o "] * user_size_choice)
    flattened_list = [item for sublist in gameboard for item in sublist]

flattened_list = [item for sublist in flattened_list for item in sublist]
chunks = [flattened_list[x:x+user_size_choice +1 ] for x in range(0, len(flattened_list), user_size_choice + 1)]
print(chunks)

for row in chunks:
    print(" ".join(map(str,row)))
