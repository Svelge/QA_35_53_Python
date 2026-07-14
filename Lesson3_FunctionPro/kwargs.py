# ** - это словарь
#1
def print_config(**kwargs):
    print(type(kwargs), kwargs)

print(print_config(browser="chrome", headless=True, TimeOut=30))
print(print_config())

#2
def create_user(**data):
    return data

user = create_user(name="Anna",role="admin")
print(user)

#3
def example(a,b=10,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

example(1,2,3,4,5,name="Anna")

