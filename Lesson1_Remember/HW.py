def print_substring_reverse(s,start,finish):
    if s is None or s.strip()=="":
        print("Wrong args")
        return
    if start<0 or finish>=len(s) or start>finish:
        print("Wrong args")
        return
    beginning = s[:start]
    middle_reversed = s[start:finish+1][::-1] # [::-1] - задом наперед
    end = s[finish+1:]
    print(beginning+middle_reversed+end)
print_substring_reverse("Shalom",1,3)
print_substring_reverse(None,1,3)
print_substring_reverse("Hi",1,5)
print_substring_reverse("hi",3,1)

def get_words_reverse(s):
    words = s.split()
    reversed_words = words[::-1]
    return "".join(reversed_words)

print()
print(get_words_reverse("Hello my nice world"))

def print_words_revers_in_column(s):
    words = s.split() #разделяем слова
    for word in words:
        print(word[::-1]) #берем каждое слово и разворачиваем

print()
print_words_revers_in_column("Hello my nice world")

