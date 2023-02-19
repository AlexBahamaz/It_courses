# Богомаз Алексей
"""
Парсит данные с биржи Binance BTC/USDT за последние 60 дней
и создаёт pandas dataSet с этими данными
Определяет динамику стоимости в % и вносит в dataSet.
Рисует график свечей за заданный период с указанием Тренда стоимости

"""
import matplotlib.pyplot as plt
import tkinter as tk
import pandas as pd
import urllib.request
import datetime as dt
from binance.client import Client # pip install python-binance

class InternetChecker():
    
    @staticmethod
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False

class DataMaker():

    @staticmethod
    def get_historical_ohlc_data(symbol,past_days=30,interval='1h'): #past_days: how many days back to download the data, interval - what the interval to download 1d, 1h
        client = Client()
        start_str=str((pd.to_datetime('today')-pd.Timedelta(str(past_days)+' days')).date())
        
        dataSet = pd.DataFrame(client.get_historical_klines(symbol=symbol,start_str=start_str,interval=interval)) #using api to get dataset
        
        dataSet.columns = ['open_time','open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades', 'taker_base_vol', 'taker_quote_vol','is_best_match']
        dataSet = dataSet.astype({'open':'float', 'close':'float', 'high':'float', 'low':'float'})
        dataSet['open_date_time'] = [dt.datetime.fromtimestamp(x/1000) for x in dataSet.open_time]
        dataSet['symbol'] = symbol
        dataSet['dinamics_percent'] = (dataSet['close'] - dataSet['open']) / dataSet['open'] * 100
        #dataSet= dataSet[['symbol','open_date_time','open', 'high', 'low', 'close', 'volume', 'num_trades', 'taker_base_vol', 'taker_quote_vol']]
        dataSet = dataSet[['symbol', 'open_date_time','dinamics_percent','open', 'close', 'high', 'low' ]]
        return dataSet
           
class DrawGraph(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Binance Analytics')
        if InternetChecker.connect():
            lab_1 = tk.Label(self, text='Hello friend!')
            lab_2 = tk.Label(self, text="Let's play with some Bitcoins!")
            button_1 = tk.Button(self, text="Let's the show begin", command=lambda: self.__candleStickChartMaking(DataMaker.get_historical_ohlc_data("BTCUSDT", 60, '1d')))
            lab_1.grid(row=0, column=0, padx=10, pady=10)
            lab_2.grid(row=1, column=0, padx=10, pady=10)
            button_1.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        else:
            lab_1 = tk.Label(self, text='Please, check your internet connection!')
            lab_1.grid(row=0, column=0, padx=10, pady=10)

    def __candleStickChartMaking(self, data):
        width_1 = .4
        width_2 = .04
        bull_dataFrame = data[data.close >= data.open]
        bear_dataFrame = data[data.close < data.open]
        print(len(bull_dataFrame))
        print(len(bear_dataFrame))
        if len(bull_dataFrame) > len(bear_dataFrame):
            plt.title('Тренд восходящий')
        elif len(bull_dataFrame) < len(bear_dataFrame):
            plt.title('Тренд нисходящий')
        else: plt.title('Тренд равновесный')
        plt.bar(bull_dataFrame.open_date_time, bull_dataFrame.close-bull_dataFrame.open, width_1, bottom=bull_dataFrame.open, color='green')
        plt.bar(bull_dataFrame.open_date_time, bull_dataFrame.high-bull_dataFrame.close, width_2, bottom=bull_dataFrame.close, color='green')
        plt.bar(bull_dataFrame.open_date_time, bull_dataFrame.low-bull_dataFrame.open, width_2, bottom=bull_dataFrame.open, color='green')
        plt.bar(bear_dataFrame.open_date_time, bear_dataFrame.close-bear_dataFrame.open, width_1, bottom=bear_dataFrame.open, color='red')
        plt.bar(bear_dataFrame.open_date_time, bear_dataFrame.high-bear_dataFrame.open, width_2, bottom=bear_dataFrame.open, color='red')
        plt.bar(bear_dataFrame.open_date_time, bear_dataFrame.low-bear_dataFrame.close, width_2, bottom=bear_dataFrame.close, color='red')
        plt.grid()
        plt.xticks(rotation=30, ha='right')
        plt.show()

if __name__ == "__main__":
    
    graphDrawing = DrawGraph()
    graphDrawing.mainloop()