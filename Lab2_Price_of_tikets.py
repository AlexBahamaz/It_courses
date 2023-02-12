#Богомаз Алексей
#lab2 Стоимости билетов

class Ticket_common_class:
    __price_of_1kg_luggage = 12 #приватный атрибут класса
    __price_of_range_1km = 0.5
    
    def __init__(self, range_km, luggage_kg, insurance = 250, class_id = 3):
        self.range_km = range_km
        self.luggage_kg = luggage_kg
        self.insurance = insurance
        self.class_id = class_id
    
    @property # Устанавливаем сеттеры
    def range_km(self):
        return self.__range_km
    
    @range_km.setter 
    def range_km(self, range_km):
        if (range_km!= 0):
            self.__range_km = range_km
    
    @property
    def luggage_kg(self):
        return self.__luggage_kg
    
    @luggage_kg.setter 
    def luggage_kg(self, luggage_kg):
        if (luggage_kg != 0):
            self.__luggage_kg = luggage_kg
    
    @property
    def insurance(self):
        return self.__insurance
    
    @insurance.setter 
    def insurance(self, insurance):
        if (insurance != 0):
            self.__insurance = insurance
    
    @property
    def class_id(self):
        return self.__class_id
    
    @class_id.setter 
    def class_id(self, class_id):
        if (class_id != 0):
            self.__class_id = class_id
    
    def price(self):
        return self.__range_km * self.__price_of_range_1km + self.__luggage_kg * self.__price_of_1kg_luggage + self.__insurance
    
    def info(self):
        print()
        print('В стоимость билета ' + str(self.__class_id) + ' класса включено:')
        print('--------------------------------------')
        print('За ' + str(self.__range_km) +' км полёта ' + str(self.__range_km * self.__price_of_range_1km) + '$')
        print('За ' + str(self.__luggage_kg) +' кг богажа ' + str(self.__luggage_kg * self.__price_of_1kg_luggage) + '$')
        print('За страховку ' + str(self.__insurance) +' $')
        print('--------------------------------------')
        print('Итого: ' + str(self.price()) +' $')
    
ticket_3_st_class = Ticket_common_class(1000, 100, 150, 3)
ticket_3_st_class.info()

class Ticket_2st_class(Ticket_common_class): # Наследуем от Ticket_common_class
    __price_of_meal = 450
    def __init__(self, range_km, luggage_kg, insurance, class_id, number_of_meals):
        super().__init__(range_km, luggage_kg, insurance, class_id) # Наследуем метод __inin__ от Ticket_common_class
        self.number_of_meals = number_of_meals
        
    @property
    def number_of_meals(self):
        return self.__number_of_meals
    
    @number_of_meals.setter 
    def number_of_meals(self, number_of_meals):
        if (number_of_meals != 0):
            self.__number_of_meals = number_of_meals
        
    def price(self):
        return super().price() + self.__number_of_meals * self.__price_of_meal # Наследуем метод price() от Ticket_common_class
    
    def info(self):
        super().info()
        print('Сюда включены дополнительные услуги:')
        print('----------------------')
        print('За ' + str(self.__number_of_meals) +' приёмов пищи ' + str(self.__number_of_meals * self.__price_of_meal) + '$')
    
ticket_2st_class = Ticket_2st_class(1000, 100, 150, 2, 2)
ticket_2st_class.info()

class Ticket_1st_class(Ticket_2st_class):
    
    __one_bootle_price = 550
    
    def __init__(self, range_km, luggage_kg, insurance, class_id, number_of_meals, bottles_of_beer):
        super().__init__(range_km, luggage_kg, insurance, class_id, number_of_meals)
        self.bottles_of_beer = bottles_of_beer

    @property
    def bottles_of_beer(self):
        return self.__bottles_of_beer
    
    @bottles_of_beer.setter 
    def bottles_of_beer(self, bottles_of_beer):
        if (bottles_of_beer != 0):
            self.__bottles_of_beer = bottles_of_beer
        
    
    def price(self):
        return super().price() + self.__bottles_of_beer * self.__one_bootle_price
    
    def info(self):
        super().info()
        print('За ' + str(self.__bottles_of_beer) +' бутылки пива ' + str(self.__bottles_of_beer * self.__one_bootle_price) + '$')
    
    
ticket_1st_class = Ticket_1st_class(1000, 10, 600, 1 ,2, 4)
ticket_1st_class.insurance = 1280
ticket_1st_class.info()

     
