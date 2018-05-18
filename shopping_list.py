# make a list to hold onto our items
shopping_list = []
 
def show_help():
    # Print out instructions on how to use this app
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to view the current list of items.
""")

def show_list():
    # print out our list
    print("Here's your list:")

    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

def remove_from_list():
    show_list()
    what_to_remove= input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

show_help()

while True:
    # ask for new items
    new_item = raw_input("> ")
    
    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue

    # be able to show the items in the list
    if new_item == 'SHOW':
        show_list()
	continue
    elif new_item.upper() == "REMOVE":
        remove_from_list()
    else:
        add_to_list(new_item)

show_list()
