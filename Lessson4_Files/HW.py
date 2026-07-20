print("#1")

def save_shopping_list(items):
    with open("shopping.txt",'w',encoding='utf-8') as file:
        for item in items:
            file.write(item+"\n")

items = [
"Milk",
"Bread",
"Apples",
"Coffee"
]

save_shopping_list(items)
print()

print("#2")

import csv

with open("students.csv","w",encoding="utf-8",newline="") as file:
    writer=csv.writer(file)

    writer.writerow(["Name","Age"])
    writer.writerow(["Anna",21])
    writer.writerow(["Tom",19])
    writer.writerow(["Kate",22])

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Students:{row['Name']} ({row['Age']})")

print("#3")

import json


def save_profile(name,age,city):
    profile = {
        "name": name,
        "age": age,
        "city": city
    }

    with open('profile.json','w',encoding='utf-8') as file:
        json.dump(profile,file,indent=2,ensure_ascii=False)

    with open("profile.json", "r", encoding="utf-8") as file:
        loaded_profile = json.load(file)
        print(loaded_profile)

save_profile("Alex", 31, "Tel aviv")




