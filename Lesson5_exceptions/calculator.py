#low level - it performs only calculations
#no interaction with the user

def calculate(a:float,b:float,op:str):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op =='*':
        return a*b
    elif op == "/":
        return a/b #zerodivision error if b == 0
    else:
        raise ValueError(f"Unknown action:{op}")

#Middle level - parsing. Convert string into numbers.

def pars_and_calc(a_str:str,b_str:str,op:str): #превращаем стринг во float
    a = float(a_str) #ValueError of not number
    b = float(b_str) #ValueError of not number
    return calculate(a,b,op)

# TOP LEVEL - dialogue. It captures everything and explains it to the user.

def run_calculator():

    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        op = input("Enter action(+,-,*,/): ")
        result = pars_and_calc(a,b,op)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Invalid data: {e}")
    except ZeroDivisionError:
        print("You can't divide by 0!")

run_calculator()

print()

def is_number(text):
    try:
        float(text)
        return True
    except (TypeError, ValueError):
        return False

print(is_number("314"))
print(is_number("3.14"))
print(is_number ("3,14"))
print(is_number("Hello"))
print(is_number(None))

print()

try:
    value = int("25")
except ValueError:
    print("This is not a number")
else:
    print("The transformation was successful: ", value)
finally:
    print("This block is always executed")