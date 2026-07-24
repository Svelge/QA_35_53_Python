print("#1")

def get_list_element(items,index):
    if index >= len(items):
        return "Index out of range"
    else:
        return items[index]


numbers = [10, 20, 30]
print(get_list_element(numbers, 1))
print(get_list_element(numbers, 10))

def get_list_element(items,index):
    try:
        return items[index]
    except IndexError:
        return "Index out of range"

numbers = [10, 20, 30]
print(get_list_element(numbers, 1))
print(get_list_element(numbers, 10))
print()

print("2")

def get_user_data(user,key):
    try:
        return user[key]
    except KeyError:
        return "Key was not found"

user = {
        "name":"Anna",
        "age":30
    }
print(get_user_data(user, "name"))
print(get_user_data(user, "email"))

print()

print("#3")

def calculate_average(first_value,second_value):
    if first_value is None or second_value is None:
        return "Invalid data type"
    else:
        try:
            a = float(first_value)
            b = float(second_value)
            return (a + b) / 2
        except ValueError:
            return "Value must be a number"

print(calculate_average("10", "20"))
print(calculate_average("hello", "20"))
print(calculate_average(None, 20))
print()

print("#4")
def read_number():
    try:
        value = int(input("Print any number "))
        print("Number was entered successfully")
    except ValueError:
        print('Invalid number')
    finally:
        print('Program finished')

read_number()

print()

def validate_age(age):
    if age<0:
        raise ValueError("Age cannot be negative") #raise сам бросает ошибку
    if age>120:
        raise ValueError("Age is not realistic")

# validate_age(25)
# validate_age(-5)
# validate_age(165)

try:
    validate_age(25)
except ValueError as error:
    print(error)

try:
    print(validate_age(-5))
except ValueError as error:
    print(error)

try:
    print(validate_age(165))
except ValueError as error:
    print(error)