#Богомаз Алексей

import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
import urllib.request

class InternetChecker():

    @staticmethod
    def connect(url_check='http://google.com'):
        try:
            urllib.request.urlopen(url_check)
            return True
        except:
            return False


class Window(tk.Tk):
    __ulr_example = "https://www.python.org/"
    __labels = "Введите адрес веб-сайта:"
    __state_of_buttons = tk.NORMAL
    __state_of_Internet = ''


    @classmethod
    def switchButtonState(cls):
        if InternetChecker.connect():
            cls.__state_of_buttons = tk.NORMAL
            cls.__state_of_Internet = 'You have a good Internet connection!!!'
        else:
            cls.__state_of_buttons = tk.DISABLED
            cls.__state_of_Internet = 'Check your internet connection!!!'


    def __init__(self):
        super().__init__()
        self.title("Форма для расчёта")      
        text_field = tk.Text(width=80, height=1)
        #self.after(1000, self.switchButtonState()) 
        self.switchButtonState()
        text_field.insert(1.0, self.__state_of_Internet)
        label = tk.Label(text=self.__labels, anchor="e",)
        label.grid(row=0, column=0, sticky='e', padx=10, pady=10)
        __entry = tk.Entry(width=40, textvariable=self.__ulr_example)
        __entry.insert(0, self.__ulr_example)
        __entry.grid(row=0, column=1, sticky='e', padx=10, pady=10)
        self.btn_sub=tk.Button(state=self.__state_of_buttons,
                          text='Сохранить',
                          command=lambda: self.saveClick(__entry))
        self.btn_sub.grid(row=1, column=1, sticky='e', padx=10, pady=10)
        text_field.grid(row=2, column=0, columnspan=2, padx=10, pady=10)



    def saveClick(self, entry):
        url = entry.get()
        if InternetChecker.connect(url):
            urllib.request.urlretrieve(url, asksaveasfilename(initialdir="~/Documents/It_courses/Home_Work/Tkinter_examples",
                                                              defaultextension=".html",
                                                              initialfile="test.html"))
        else:
            messagebox.showerror('Ошибка', 'Ошибка: Проверьте правильность введённого адреса')

    
if __name__ == "__main__":

    window = Window()
    window.mainloop()
