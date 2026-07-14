books = {
    'Harry Potter and .....':'J.K.Rowling',
    'To kill a mockingbird':'Harper Lee'
}

books1 = {
    'Harry Potter and .....',
    'To kill a mockingbird'
}
print(books1)

response = {
    'status':'success',
    'user':{'id':1,'name':'Alex'}
}

print(response['user']['name'])

data = [1,22,3]
print(isinstance(data,list)) #проверка типа данных

value = 10
print(type(value))
print(isinstance(value,(int,float)))

team_ages = {
    "Alex":31,
    "Petr":40,
    "Olga":26,
    "Lisa":30
}
print(team_ages.keys()) # keys = name
print(team_ages.values()) # values = age


team_names = ['Alex', 'Petr', 'Olga', 'Lisa']
team_numbers = [31, 40, 26, 30]
team_ages = {name:age for name,age in zip(team_names,team_numbers)}
print(team_ages)