#Богомаз Алексей
import csv

filename = "20_02_23_b_data.csv"
# список покупок: вес и стоимость
shoplist = {"яблоки": [30, 40 ], "масло": [50, 60 ], "рис ": [60, 70]}

# Запись в файл
with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "weight", "price"], quoting=csv.QUOTE_ALL)
    writer.writeheader()  # Записывает заголовки в файл
    for name, values in sorted(shoplist.items()):
        writer.writerow(dict(name=name, weight=values[0], price=values[1]))

#Чтение из файла
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)