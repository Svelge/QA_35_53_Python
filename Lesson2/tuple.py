numbers_tuple = (1,2,3,4,5,3,9,7)
my_tuple=([1,2,3],['a','b','c'])

first_element = numbers_tuple[0]
nested_tuple = (1,2,(3,4),5)
print(nested_tuple[2])
print(nested_tuple[2][1]) # здесь указываем индекс внутри тапла и дальше уже индекс из списка

tuple1 = (1,2,3)
tuple2 = (1,2,3)
tuple3 = (4,5,6)
print(tuple1==tuple2)
print(tuple2==tuple3)
my_tuple = (1,2,3,4,5)
print(3 in my_tuple)
print(33 in my_tuple)

for el in my_tuple:
    print(el)

i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i+=1

tuple1 = (1,2,3)
tuple2 = (1,2,3)
conc_tuple = tuple1 + tuple2
print(conc_tuple)

my_tuple=(1,2,3,4,5,6)
length_of_tuple = len(my_tuple)
print(length_of_tuple)

sum_of_elements = sum(my_tuple)
print(sum_of_elements)

max_element = max(my_tuple)
min_element = min(my_tuple)
print(min_element)
print(max_element)
my_tuple1 = ()
print(len(my_tuple1))
print(sum(my_tuple1))
# print(max(my_tuple1))
# print(min(my_tuple1))

original_tuple = (3,1,4,1,5,6,8,4,2,1,6,3,2)
sorted_tuple = tuple(sorted(original_tuple))
print('Original: ', original_tuple)
print('Sorted: ', sorted_tuple)

my_tuple = list(original_tuple)
print(my_tuple)
print("Original: ",original_tuple)

my_string = "".join(map(str,original_tuple))
print(my_tuple)

my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)
my_list[2] = 10
updated_tuple = tuple(my_list)
print("Original: ", my_tuple)
print("Updated: ", updated_tuple)

