# Write your code here :-)
price_list = {"rice":6, "dall" : 8,"sugar": 3,"snacks":1}
print(price_list)
print(price_list["dall"])


for item in price_list:
   # print(item)

    print(item+"=$"+str(price_list[item]))

cart = True

while cart:
    item = input("Enter the name :")
    if item == 'End':
       cart = False
    else:
        quantity = int(input("Enter the quantity :"))
        item_price = int(price_list[item] * int(quantity)
        print(item+':' + str(price_list[item]) + 'X' +str(quantity)+ '='+ int(print_list[item]*int(quantity)))


