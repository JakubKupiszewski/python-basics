name_set = set()
name_set.add("Kamil")
name_set.add("Kuba")

name_set2 = {"Mariusz", "Wojtek"}

name_set.update(name_set2)
#można również extend

for name in name_set:
    print(name)

