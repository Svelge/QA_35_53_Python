with open("users.txt", "w", encoding="utf-8") as file:
    file.write("Tony\n")
    file.write("Ivan\n")
    file.write("Anna\n")

#read() - читает файл целиком в одну строку, включая все переносы строк внутри
with open("users.txt","r", encoding="utf-8") as file:
    content = file.read()
print(content)
print(len(content))
#для небольших файлов

#readlines() - возвращает список, где каждый элемент - одна строка файла
#могут на интервью спросить
with open("users.txt","r", encoding="utf-8") as file:
    lines = file.readlines()
print(lines)
#возвращает список и можно по каждому элементу пройтись

for line in lines:
    print(line.strip()) #strip - убирает пробелы по краям и \n (вайт пробельные символы)
#for не записывает в память, если файл тяжелый - можно просто вынимать поочередно
print()

with open("users.txt","r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


