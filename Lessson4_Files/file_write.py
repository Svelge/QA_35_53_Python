with open("greeting.txt","w",encoding="utf-8") as file:
    file.write("Hello, automated tests!\n")
    file.write("Second line\n")
    #open - если файл есть - ог откроется, если нет - он создастся.
    # Если есть и в нем что-то есть - текст исчезнет и запишется строчка под write
    # w - write
    #encoding - будет брать по умолчанию кодировку ОС на которой запущен код
    #utf-8 - самая распространенная кодировка
    # "r" - read
    # "w" - write - создает или перезаписывает
    # "a" - append - дозапись, добавляет новые строчки, если файла нет - создаст
    # "r+" - read and write
    # "rb", "wb" - pdf, screenshots

with open("greeting.txt", "a", encoding="utf-8") as file:
    file.write("Testing Append")

def log_test_result(test_name,status):
    with open("test_run.log","a",encoding="utf-8") as log_file:
        log_file.write(f"{test_name}:{status}\n")

log_test_result("test_login", "PASSED")
log_test_result("test_registration", "FAILED")
log_test_result("test_logout", "PASSED")


