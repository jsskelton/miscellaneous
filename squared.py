def squared(num):
    try:
        num1 = (int(num) ** 2)
	print(num, num1)
        return num1
    except:
	print(num * len(num))
        return num
    
squared("five5")

