import matplotlib.pyplot as plt
import matplotlib as mpl
import tkinter as tk
import numpy as np


class DataMaker():

    __Cxp = [round(i, 2) for i in np.arange(0.01, 0.1, 0.01)]
    __Cy = [round(i, 2) for i in np.arange(0.1, 1, 0.1)]
    __S = 0.47 # m2
    __V = 27 # m/c
    __ρ = 1.23

    @staticmethod
    def createPlaneList_X(max_x, step_x): 
        return list(map(lambda x: x, [i for i in range(0, max_x + 1, step_x)]))

    @staticmethod
    def createPlaneList_Y(max_y,step_y):
        return list(map(lambda x: x, [i for i in range(0, max_y + 1, step_y)]))
    
    @staticmethod
    def createList_Xp(Cxp=__Cxp, V=__V, S=__S, ρ=__ρ):
        return [i*((ρ*V**2)/2)*S for i in Cxp]
    
    @staticmethod
    def createList_Ya(Cy=__Cy, V=__V, S=__S, ρ=__ρ):
        return [i*((ρ*V**2)/2)*S for i in Cy]
           

class DrawGraph(tk.Tk):

    __list_x = DataMaker.createPlaneList_X(100, 1)
    __list_y = DataMaker.createPlaneList_Y(100, 1)
    __list_Xp = DataMaker.createList_Xp()
    __list_Ya = DataMaker.createList_Ya()
    __lbl_Xp = 'aэродинамическое сопротивление'
    __lbl_Ya = 'подъемная сила'
    
    def __init__(self):
        super().__init__()
        self.title('It-academy graph')
        #self.geometry("500x500")
        lab_1 = tk.Label(self, text='Hello friend!')
        lab_2 = tk.Label(self, text='Choose what a chart for random do you need:')
        button_1 = tk.Button(self, text="Linear", command=lambda: self.__graphMaking("linear")) #lambda потому что в command нельзя устанавливать аргументы
        button_2 = tk.Button(self, text="Bar", command=lambda: self.__graphMaking("bar"))
        lab_3 = tk.Label(self, text='Choose what a chart do you need for Xp to Ya')
        button_3 = tk.Button(self, text="Linear", command=lambda: self.__graphMaking("linear","My linear chart", self.__lbl_Xp, self.__lbl_Ya, self.__list_Xp, self.__list_Ya))
        button_4 = tk.Button(self, text="Bar", command=lambda: self.__graphMaking("bar","My bar chart", self.__lbl_Xp, self.__lbl_Ya, self.__list_Xp, self.__list_Ya))
        lab_1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        lab_2.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        button_1.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        button_2.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
        lab_3.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        button_3.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')
        button_4.grid(row=4, column=1, padx=10, pady=10, sticky='nsew')
   

    def __graphMaking(self, type_of_graph = "linear" ,text_title = 'My random chart', label_x="Value of x", label_y="Value of y", data_x=__list_x, data_y=__list_y):
        plt.ion()
        plt.clf() # очистка фигуры если в ней был график
        mpl.is_interactive()
        if type_of_graph == "linear":
            plt.plot(data_x, data_y) 
        elif type_of_graph == "bar":
            plt.bar(self.__list_x, self.__list_y)
        plt.title(text_title)
        plt.xlabel(label_x)
        plt.ylabel(label_y)
        plt.show()

if __name__ == "__main__":
    
    graphDrawing = DrawGraph()
    graphDrawing.mainloop()