from pathlib import Path

data_folder = Path("test_data") # создаем папку через объект path
file_path = data_folder/"users.csv" # получаем путь к файлу, слэш это оператор, он соединяет части пути и он сам определяет систему и ставит слэш в нужном направлении
print(file_path)

print(file_path.exists()) # exists проверяет есть ли вообще такой путь

screenshots_folder = Path("screenshots")
screenshots_folder.mkdir(exist_ok=True) # если папка есть - не поднимай никаких ошибок, просто ничего не делай
reports_folder = Path("reports/2026")
reports_folder.mkdir(parents=True,exist_ok=True) #parents True говорит что надо создать все папки на пути

