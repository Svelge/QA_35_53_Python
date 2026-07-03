name = 'Alice'
age = 30
formatted_string=f"Hello my name is {name} and I am {age} years old"
print(formatted_string)

#*****
#find()
s = 'AbrakadabraAbrakadabra'
str ='bra'
print(s.find(str)) #индекс с начала
print(s.rfind(str)) #индекс с конца
print(s.find('add'))
#*******
#count(sub[start,end])
print(s.count(str))
print(s.count(str,4))
print(s.count(str,4,15))
#**************
#str.upper()
#str.lower()
s = 'AbrakaDabRaAbrakaDabra'
print(s.lower())
print(s.upper())
print(s)

#*****************
s='Cat, Dog, Hamster Rabbit, Pig'
print(s.split())
print(s.split(','))
print(s.split(',',3))

#*************
#rjust() & ljust()
s = "Hi!"
print(s.rjust(10,'*')) #just - увеличивает количество символов (количество, символы)
print(s.ljust(10,'*'))

test = ["Login", "Cart", "API"]

for t in test:
    print(t.ljust(15), 'OK')

order = "125"
print(order.rjust(8,"0"))

#****************
s = 'AbrakaDabRaAbrakaDabra'
print(s.isalpha())
s1 = "123456"
print(s.isdigit())
print(s1.isdigit())

#******************
#index()
# text = 'I like Java'
# pos = text.index("automation",10)
# print(pos)
#######
#replace()
text = 'I like Java'
print(text.replace("Java","Python"))

text = "2026-07-03"
new_text = text.replace("-","/")
print(text)
print(new_text)


