



# через звездочку по сути передается кортеж элементов в любом количестве
# 1 звездочка * это тапл
#2
def print_scores(student,*scores):
    print(f"Student: {student}")
    print("Scores: ",scores)

print_scores("Anna", 90,85,100)
print_scores("Bob",75)

print()

#3
def check_status_codes(*codes):
    for code in codes:
        assert code==200

print(check_status_codes(200,200,200))
# print(check_status_codes(200,404,200)) - assertionError