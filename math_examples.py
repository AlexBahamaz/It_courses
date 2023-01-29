import math
import scipy.constants as const

def energy(m:float): # Energy in Joules(kg*(m/s)**2)
  return m * pow(const.speed_of_light, 2) #mass in kilograms(kg)

sphere_volume = lambda r: 4 / 3 * math.pi * pow(r, 3)
area_of_a_circle = lambda r: math.pi * pow(r, 2)

print("Энергия равна ", energy(float(input("Введите массу в килограммах = "))), " Дж")
print("Объм шара равен = ", round(sphere_volume(float(input("Введите радиус шара = "))), 2))
print("Площадь круга равна =", round(area_of_a_circle(float(input("Введите радиус круга = "))), 2))