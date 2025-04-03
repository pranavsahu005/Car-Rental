from Entity.Car import Car
class CarService:
    def __init__(self):
        self.__cars=[]
    def addCars(self,car):
        self.__cars.append(car)
    def  displayCars(self):
        return self.__cars
    def removeCar(self,index):
        self.__cars.pop(index)
    def searchCar(self,num):
        for item in self.__cars:
            if(num==item.getCarno()):
                return item
        return None

