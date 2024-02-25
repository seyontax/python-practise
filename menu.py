# Write your code here :-)
menu = {"hopper" : "5","puttu" : "10" , "thosai" : "12", "Iddley": "20"}
print(menu)
print(menu["thosai"])

for item in menu:
 #   print(item)
 #   print(str(menu[item]))
    print(item + " = $ " + menu[item])


grand_total = []
all_line_item = []

basket = True

while basket:
    item = input("Enter the name of item :")
    if item == 'end':
        basket = False
    else:
        quantity = int(input("Enter the quantity : " ))
        item_pric = int(str(menu[item])) "X" int(quantity)



