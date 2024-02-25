# Write your code here :-)
import sys

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = datetime.date()
current_date = date.strfdate("%Y:%M:%D")

print("current_time:",current_time)


print("Seyon Tax Inc.",  )

input_file = open('pricelist.csv','r')

all_itmes = input_file.readlines()

price_list = {}

for item in all_itmes:
    item_name = item.split(",")[0]
    print(item)

