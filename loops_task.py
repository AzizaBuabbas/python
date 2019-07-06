list_of_items = []
item_name = ""
while item_name != "done":
	item_name = input("Item (enter \"done \" when finished):")
	if item_name == "done":
		break

	price = input ("price:")
	quantity = input ("quantity:")

	item = {
	      "name": item_name,
	      "price": price ,
	      "quantity": quantity 
	}
	list_of_items.append(item)

print("==========")
print("Reccipt")
print("==========")

total = 0
for x in list_of_items:
    print("%s %s %.2fKD" % (x["quantity"], x [ "name"],(float(x["price"])*int(x["quantity"]))))
    total = total + (float(x["price"])*int(x["quantity"]))



print("Total: %s"% total)
