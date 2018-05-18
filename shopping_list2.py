# make a list to hold onto our items
shopping_list = []
 
# print out instructions
print("What shoudl we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

while True:
    # ask for new items
    new_item = input("> ")
    
    # be able to quit the app
    if new_item == 'DONE':
        break

    # be able to quit the app
    if new_item == 'SHOW':
        break

    # be able to quit the app
    if new_item == 'HELP':
        break

    # add new items to our list
    shopping_list.append(new_item)

# print out our list
print("Here's your list:")

for item in shopping_list:
    print(item)
