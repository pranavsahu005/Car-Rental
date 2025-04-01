class Car:
    def __init__(self,carno='',name='',seater=0):
        self.__carno=carno
        self.__name=name
        self.__seater=seater


    # setter

    def setCarno(self,value):
        self.__carno=value
    def setName(self,value):
        self.__name=value
    def setSeater(self,value):
        self.__seater=value

    #getter

    def getCarno(self):
        return self.__carno
    def getName(self):
        return self.__name
    def getSeater(self):
        return self.__seater
