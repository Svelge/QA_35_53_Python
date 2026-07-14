#1
def login(username,password):
    print(username,password)

data = ["admin","12345"]
login(data[0],data[1]) #без распаковки

(login(*data)) #распаковка // разложи список на аргументы и я разберусь что куда занести

# для словаря та же логика, распаковывает пару ключ и значение в именованные аргументы

#2
user = {
    "username":"admin",
    "password":"12345"
}


# login(**user)  - вариант с ошибкой, нету ключа remember_me
#
# user = {
#     "username":"admin",
#     "password":"12345",
#     "remember_me":True
# }
#
# login(**user)

