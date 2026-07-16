print('#1\n')
def create_profile(name,age=18,city="Unknown"):
    user_data = {
        "name":name,
        "age":age,
        "city":city
    }
    return user_data

print(create_profile("Anna"))
print(create_profile("Tom",25))
print(create_profile("Alex",31,"Tel Aviv"))

print()

print('#2\n')
def sum_even_numbers(*numbers):
    if len(numbers)==0:
        return 0
    else:
        x = 0
        for a in numbers:
            if a%2==0:
                x = x+a
        return x
print(sum_even_numbers(1, 2, 3, 4, 5, 6))
print(sum_even_numbers(7, 9))
print(sum_even_numbers())
print()

print('#3\n')

def print_pet_info(name,**info):
    print(f"Name:{name}")
    if not info:
        print("No additional information")
    else:
        for key, value in info.items():
            print(f"{key}: {value}")
print_pet_info(
    "Lucky",
    age=4,
    color="White",
    breed="Spitz"
)
print()
print_pet_info("Lucky")













