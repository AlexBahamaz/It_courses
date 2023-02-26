#Богомаз Алексей

import tkinter as tk
from tkinter import messagebox
import math as mt

class Window:

    __result_text = "ДЛЯ ВЫЧИСЛЕНИЯ ПОТРЕБНОЙ ТЯГИ СИЛОВОЙ \nУСТАНОВКИ БЛА  ВВЕДИТЕ ЗНАЧЕНИЯ \nИ НАЖМИТЕ КНОПКУ \"ВЫЧИСЛИТЬ\""
    __text_sample = "ИЗМЕНЕНИЕ ОТ ПОТРЕБНОЙ ТЯГИ СИЛОВОЙ УСТАНОВКИ ПРИ ЗАДАННОМ (Cx): "
    __labels = [
    "ВЕС Л/А(gramm): ",
    "ПЛОЩАДЬ КРЫЛА Л/А(dm2): ",
    "КОЭФФИЦИЕНТ СОПРОТИВЛЕНИЯ (Cx): ",]
    __entry = []

    def __init__(self, resizable=(False, False)):
        self.window = tk.Tk()
        self.window.title("Форма для расчёта")      
        self.window.resizable(resizable[0], resizable[1])
        self.frm_form=tk.Frame(borderwidth=4)
        self.frm_form.pack()
        self.text_field = tk.Text(width=120, height=4)
        self.text_field.insert(1.0, self.__result_text)
        for idx, text in enumerate(self.__labels):
            self.label = tk.Label(master=self.frm_form, width=50, text=text, anchor="e")
            self.__entry.append(tk.Entry(master=self.frm_form, width=50))
            self.label.grid(row=idx, column=0,)
            self.__entry[idx].grid(row=idx, column=1,)
        frm_buttons = tk.Frame()
        frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        btn_sub=tk.Button(master=frm_buttons, text='Вычислить', command=lambda: self.onClickEntry(self.__entry, self.text_field))
        btn_sub.pack(side=tk.RIGHT, padx=30)
        self.text_field.pack()

    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
    
    def onClickEntry(self, entry,text):
        lst = []
        __p=1.23
        for i in range(len(entry)):
            if self.isfloat(entry[i].get()):
                lst.append(float(entry[i].get()))
            else: 
                messagebox.showerror('Ошибка ввода', 'Ошибка: Введите численное значение')
        υ= mt.sqrt(2*lst[0]/lst[1]*__p*lst[2])
        h_p=υ/75
        Wt=h_p*735.5
        r_Wt=round(Wt/1000, 2)
        text.delete('1.0', 'end')
        text.insert(4.0, f"{self.__text_sample} {round(υ, 3)} kg/sec\n")
        text.insert(4.0, f"{self.__text_sample} {round(h_p, 3)} h/p\n")
        text.insert(4.0, f"{self.__text_sample} {round(Wt, 3)} Wt\n" )
        text.insert(4.0, f"{self.__text_sample} {round(r_Wt,3)} kWt")
    
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    window = Window()
    window.run()
