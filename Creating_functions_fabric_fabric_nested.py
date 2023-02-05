#Богомаз Алексей
#вложенный метод создания функции
def decrease_times_nested(times):
    def input_list():
        return [float(i)/times for i in input().split()]
    return input_list()

#фабричный подход создания функции
def decrease_times_fabric(times):
    def input_list():
        return [float(i)/times for i in input().split()]
    return input_list

print(decrease_times_nested(5)) #печать с помощью вложенной функции

decrease_five_input_list = decrease_times_fabric(5)
print(decrease_five_input_list()) #печать с помощью функции с фабричным подходом
