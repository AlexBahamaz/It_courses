#Богомаз Алексей
#Задача с расчётом удельной мощности авто
import random

def car_efficiency(weight, power): #функция расчёта удельной мощности авто
    return weight/power

cars_data = [[random.randint(50,500) for _ in range(10)] for j in range(2)] #заполняем двухмерный массив со случайными данными первая строка масса, вторая мощность

print([car_efficiency(cars_data[0][i], cars_data[1][i]) for i in range(len(cars_data[0]))])
