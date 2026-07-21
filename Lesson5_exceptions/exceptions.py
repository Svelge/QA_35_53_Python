# with open("user.json",'r',encoding="utf-8") as file:
#     print(file.read())

# print("start program")
# result = 10/0
# print(result)
# print("End program")

# ZeroDivisionError: division by zero

# def div_int(a,b):
#     return a/b
#
# print("start program")
# res = div_int(10,0)
# print(res)
# print('end program')

#TRY/EXCEPT
print("start program")
try: #в блок try помещается потенциально опасный код и код который связан с этим потенциально опасным кодом
    result = 10/0
    print(result)
except Exception as e:
    print("An error occurred:" ,e)

print("End program")
