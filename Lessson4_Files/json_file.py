#dumps() - Python -> Json-строка (работает со строкой)
#loads() - превращается текст JSON -> в Python объект (работает со строкой)
#dump() - сохраняет Python объект в файл в формате .json (работает с файлом)
#load() - Json.file -> Python (работает с файлом)

import json

user = {"username":"Egor", "age":30, "is_admin":True}

json_string = json.dumps(user)
print(json_string)
print(type(json_string))


#обратно развернем:
user = json.loads(json_string)
print()
print(user)
print(type(user))
print(user["username"])

test_config = {
    "base_url":"https://api.example.com",
    "timeout":10,
    "retries":3
}

with open("config.json","w",encoding="utf-8") as file:
    json.dump(test_config,file,indent=2, ensure_ascii= False)

with open("config.json","r",encoding="utf-8") as file:
    loaded_config = json.load(file)

    print(loaded_config)
    print(loaded_config['base_url'])
    print(f"base_url: {loaded_config['base_url']}")

#indent - отступы для читаемости
#ensure_ascii= False - разрешает писать кириллицу