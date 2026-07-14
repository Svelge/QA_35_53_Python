#1
from operator import index

user_list = input("Enter values using space button: ")
lst = user_list.split()
if not lst:
    print("Wrong list")
else:
    print(lst[::-1])

#1.1
def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or len(lst)==0: #важен порядок // len(lst)==0 or not lst - одинаковая проверка
        print("Wrong list")
        return
    reversed_lst = lst[::-1] #:: = значит от первого к последнему элементу, -1 значит что идти от последнего к первому
    print(reversed_lst)
print_list_reverse([1,2,3,4,5])


#2
def is_valid_point(point):
    if point is None or point == ():
        return False
    if not isinstance(point, tuple):
        return False
    if len(point) != 2:
        return False
    if not isinstance(point[0],(int,float)) or not isinstance(point[1],(int,float)):
        return False

    return True

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))

#2.1

def is_valid_point(point):
    if point is None:
        return False
    if not isinstance(point, tuple):
        return False
    if len(point) != 2:
        return False
    x,y = point
    if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
        return False

    return True

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))


#3
def sublist(lst1,start,finish):
    if lst1 is None or lst1 == []:
        print("Wrong args")
        return
    if not isinstance(lst1, list):
        print("Wrong args")
        return
    if not isinstance(start, int) or not isinstance(finish,int) or start > finish:
        print("Wrong args")
        return
    if start < 0 or finish >= len(lst1):
        print("Wrong args")
        return

    middle_part = lst1[start:finish + 1]
    reversed_middle = middle_part[::-1]
    final_list = lst1[:start] + reversed_middle + lst1[finish + 1:]
    print(final_list)

sublist([10, 20, 30, 40, 50, 60], 1, 4)

#4 advanced
def get_students_by_grade(students):
    if students is None or not isinstance(students, dict) or len(students)==0:
        return{}
    result = {}
    for name,grade in students.items():
        result.setdefault(grade,[]).append(name)

        #if grade not in result:
        #   result[grade] = []
        #   result[grade].append(name)
    return result

print(get_students_by_grade({"Alice": 90,"Bob": 80, "Diana": 85, "Charlie": 79}))









