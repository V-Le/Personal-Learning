groceries = []
item = ""
i = 0

while item != "exit":
    item = str(input("What do you want to add? Type 'exit' to quit: "))

    if item == "exit":
        break
    elif item == "remove":
        remove = int(input("Which number would you like to remove? "))
        groceries.pop(remove - 1)
    else:
        groceries.append(item)
        print("Current items in the list: \n")
    for i in range(len(groceries)):
        print(i + 1, ".", groceries[i])

print("\n")
print("\nItems on the list:")
for i in range(len(groceries)):
    print(i + 1, ".", groceries[i])
