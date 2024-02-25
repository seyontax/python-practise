# Write your code here :-)
import os
print(os.listdir("."))
print(dir(os))


all_files = os.listdir(".")
counts = len(all_files)
print(counts)


for item in all_files:
    print(item)
    if item.endswith("py"):
        print(item)

