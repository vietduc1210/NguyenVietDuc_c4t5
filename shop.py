choice = input("Welcome to our shop, what do you want (C, R, U, D)?")
our_items = ['T-Shirt','Sweater']

choice = input("Welcome to our shop, what do you want (C, R, U, D)?")
if choice == "R":
   print("Our items :", sep = " ", end = "\t")
   print(*our_items, sep = ", ")

choice = input("Welcome to our shop, what do you want (C, R, U, D)?")
if choice == "C":
    new_item = input("Enter new item :")
    our_items.append(new_item)
    print("Our items :", sep=" ", end="\t")
    print(*our_items, sep=", ")

choice = input("Welcome to our shop, what do you want (C, R, U, D)?")
if choice == "U":
    update_position = int(input("Update position ? ")) - 1
    new_item = input("New item ?")
    our_items[update_position] = new_item
    print("Our items :", sep=" ", end="\t")
    print(*our_items, sep=", ")

choice = input("Welcome to our shop, what do you want (C, R, U, D)?")
if choise == "D":
    delete_position = int(input("Delete position : ")) - 1
    our_items.pop(delete_position)
    print("Our items :", sep=" ", end="\t")
    print(*our_items, sep=", ")
