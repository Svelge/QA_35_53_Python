# анонимная функция используется как аргумент к другой функции
def double(x):
    return x*2

double_lambda = lambda x: x*3 if x>0 else -x

print(double(5))
print(double_lambda(-3))

# в лямбде нельзя написать несколько строк, только одно простое выражение
# одноразовый инструмент

print()

add = lambda a,b: a+b
print(add(3,4))

is_even = lambda n: n%2 ==0
print(is_even(10))
print(is_even(7))

