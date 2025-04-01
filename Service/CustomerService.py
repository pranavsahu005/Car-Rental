from Entity.Customer import Customer
class CustomerService:
    def __init__(self):
        self.__Customers=[]
    def addCustomers(self,customer):
        self.__Customers.append(Customer)
    def  displayCustomers(self):
        return self.__Customers