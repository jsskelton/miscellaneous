def loopy(items):
    new_items = []
    for item in items:
        if "a" in item:
            continue
        else: new_items.append(item)
	print(new_items)
          
loopy(["abc","xyz"])
