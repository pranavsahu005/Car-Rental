from Entity.Customer import Customer
class CustomerService:
    def __init__(self):
        self.__Customers=[]
    def addCustomers(self,customer):
        self.__Customers.append(Customer)
    def  displayCustomers(self):
        return self.__Customers
    def removeCustomer(self,index):
        self.__Customers.pop(index)
    def searchCustomer(self,Name):
        for item in self.__Customers:
            if (Name == item.getName):
                return item
        return None
