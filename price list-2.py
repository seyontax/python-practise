# Write your code here :-)
price_list = {"rice":6, "dall" : 8,"sugar": 3,"snacks":1}
#print(price_list)
#print(price_list["dall"])


#for item in price_list:
#  print(item)

#print(item+"=$"+str(price_list[item]))

grand_total = []
all_line_items = []

cart = True


while cart:
    item = input("Enter the name :")
    if item == 'End':
       cart = False
    else:
        quantity = int(input("Enter the quantity :"))

        item_price = int(price_list[item]) * int(quantity)
        grand_total.append(item_price)

        line_item = item,':', str(price_list[item]) , 'X' , str(quantity) , '=', str(item_price)
        all_line_items.append(line_item)

for line in all_line_items:
    print(' '.join(line))

    print("Grand Total:", str(sum(grand_total)))
