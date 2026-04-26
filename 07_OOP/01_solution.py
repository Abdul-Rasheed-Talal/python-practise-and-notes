class Car:
    total_car = 0
    def __init__(self , brand , model):
        self.__brand = brand
        self.__model = model
        # self.total_car +=1
        Car.total_car +=1

    def get_brand(self):
        return self.__brand + "!"
    
    def fullName(self):
        # print(self.brand , self.model)
        return f"{self.__brand}{self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    
    

# print(my_tesla.model)
# print(my_tesla.fullName())
# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# my_tesla = ElectricCar("Tesla" , "Model S " , "85kWh")
# print(isinstance(my_tesla , Car))
# print(isinstance(my_tesla , ElectricCar))
# myCar = Car("Tata" , "Safari")
# myCar.model = "city"
# print(myCar.model)
# print(myCar.general_description())
# print(Car.general_description())
# Car("Tata" , "Nexon")
# print(safari.fuel_type())
# print(my_tesla.fuel_type())
# print(Car.total_car)


# my_car = Car("Toyota" , "Corolla")

# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("Mercedes" , "Mercedes Benz")

# print(my_new_car.brand)
# print(my_car.fullName())


class Battery:
    def batteryInfo(self):
        return "This is battery info"


class Engine:
    def engineInfo(self):
        return "This is engine info"


class ElectricCarTwo(Battery , Engine , Car):
    pass


# my_new_tesla = ElectricCarTwo("Tela" , "Model S")
# print(my_new_tesla.engineInfo())
# print(my_new_tesla.batteryInfo())
# print(my_new_tesla.model)