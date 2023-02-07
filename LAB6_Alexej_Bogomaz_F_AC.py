#Алексей Богомаз
#Расчёт F_AC
import sympy as sp
import numpy as np
import math as mt
import matplotlib.pyplot as plt

class Drag_Equation:
    def __init__(self,  S = 0.513, ρ = 1.23, C = 0.28):
        self.S = S
        self.ρ = ρ
        self.C = C
    
    def force_AC(self, V):
        C = sp.Symbol('Cx')
        return (self.C*self.S)*(self.ρ*V**2/2)
    
porshe = Drag_Equation()
speed_list = [i for i in range(2, 251, 1)]
force_AC_list =[porshe.force_AC(i) for i in speed_list]

plt.plot(speed_list, force_AC_list)
plt.grid()
plt.xlabel("Скорость, км/ч")
plt.ylabel("Аэродинамическое сопротивление")
plt.title("График кривой соотношения F_AC/V.")
plt.show()
