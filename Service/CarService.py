from Entity.Car import Car
class CarService:
    def __init__(self):
        self.__cars=[]
    def addCars(self,car):
        self.__cars.append(car)
    def  displayCars(self):
        return self.__cars
