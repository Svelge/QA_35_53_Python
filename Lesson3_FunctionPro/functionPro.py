#1
def greet(name):
    return f"Hi, {name} !"

result = greet("Alex")
print(result)

#2
def create_user(name,role="user"):    #Имя для введения, а роль дефолтная(на случай если не введено,например,но его можно менять
    return {
        "name":name,
        "role":role
    }

print(create_user("Alex"))
print(create_user("Alex","admin"))

#3
def calculate_discount(price,discount_percent=10):
    return price - (price*discount_percent/100)

print(calculate_discount(1000))
print(calculate_discount(1000,20))

# параметры без значения идут в первую очередь, а со значением всегда после них

def add_test_result(name,results=None):
    if results is None:
        results = []
    results.append(name)
    return results

print(add_test_result("test_login"))
print(add_test_result("test_logout"))

#список создается 1 раз после первого вызова

def create_user_1(username,email,role):
    return f"{username} ({email}) - {role}"
print(create_user_1("Biba","biba@gmail.com","guest"))
print(create_user_1(role = "admin", username="Mariia", email = "mariia@gmail.com"))
print(create_user_1("Mariia",role = "admin", email = "mariia@gmail.com"))