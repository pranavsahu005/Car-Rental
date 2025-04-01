class Customer:
    def __init__(self):
        self.__name=''
        self.__contact=''
        self.__city=''

    #setter

    def setName(self,value):
        self.__name=value
    def setContact(self,value):
        self.__contact=value
    def setCity(self,value):
        self.__city=value

    #getter

    def getName(self):
        return self.__name
    def getContact(self):
        return self.__contact
    def getCity(self):
        return self.__city