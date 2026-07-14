shopping_cart=['orange','peach','lemon']
empty_list = []
mixed=[2,'orange',4.22,True]
fruits = ['orange', 'peach','lemon']
print(fruits)
print(fruits[0])

fruits[1] = 'blueberry' #замена элемента по индексу
print(fruits)

list1 = ['orange', 'peach']
list2 = ['shampoo', 'soap']
comb_list = list1+list2
print(comb_list)

fruits = ['orange', 'peach','lemon']
first,second,third = fruits #можно текстом обозвать и пайтон понимает что это относится к элементу
print(first)
print(second)
print(third)

fruits = ['orange', 'peach','lemon']
for item in fruits:
    print(f"item in fruits:{item}")

correct_answers = ['orange', 'peach','lemon']
user_answers = ['orange', 'peach','lemon']

if correct_answers == user_answers:
    print("All answers are correct!")
else:
    print("Some answers are incorrect")

print(len(fruits))

numbers=[12,56,94,6]
print(max(numbers))
print(min(numbers))
print()

res = sorted(numbers)
print(res)

print(sorted(numbers, reverse=True))

word = "python"
print(sorted(word))
result = ''.join(sorted(word))
print(result)

names = ['Alexander', 'Bob', 'Tom']
print(sorted(names))
print(sorted(names, key=len))

#добавить элемент в конец списка
fruits = ['orange', 'peach','lemon']
fruits.append('orange')
print(fruits)

fruits.insert(2,'apple')
print(fruits)

first_peach_index = fruits.index('peach')
print(f"The first 'peach' was added to position:{first_peach_index}")

fruits.remove('orange')
print(fruits)

numbers = [10,20,30]
deleted = numbers.pop(1) #удали и отдай то что удалил под индексом
print(deleted)
print(numbers)

numbers.clear() #очистка списка
print(numbers)