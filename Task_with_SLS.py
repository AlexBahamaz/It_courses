#Богомаз Алексей
#Задача с расчётом и выводом силы лобового сопротивления
def resistance_force(speed): #функция расчёта силы лобового сопротивления
    return speed ** 2

[print('Для скорости',i, 'км/ч', 'CЛС =', resistance_force(float(i))) for i in input('Введите значения скорости через пробел = ').split()] #вводим данные скорости и сразу печатаем СЛС
