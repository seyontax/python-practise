# Write your code here :-
import sys

input_file = open('pricelist.csv','r')

all_itmes = input_file.readlines()

price_list = {}

for item in all_itmes:
    item_name = item.split(",")[0]
    print(item)
    item_price = item.split(",")[1]
    price_list[item_name] = item_price.strip()
print(price_list)
