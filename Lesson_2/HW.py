#1
from operator import index

user_list = input("Enter values using space button: ")
lst = user_list.split()
if not lst:
    print("Wrong list")
else:
    print(lst[::-1])

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










