from Entity.Car import Car
from Entity.Customer import Customer
from Service.CarService import CarService
from Service.CustomerService import CustomerService
Carss=CarService()
Cuss=CustomerService()
while True:
    print("*************** <SERVICES> ***************")
    print("Press 1 for CAR SERVICE !! ")
    print("Press 2 for CUSTOMER SERVICE !! ")
    print("___________________________________________")
    ch1=int(input("Enter your choice "))
    if ch1==1:
        print("Press 3 for Add  Cars !")
        print("Press 4 for Display Cars !")
        ch2=int(input("Enter your Choice !! "))
        if ch2==3:
            ob=Car()
            print("____________________________________")
            ob.setCarno(input("Enter Car number : "))
            ob.setName(input("Enter Car Name :  "))
            ob.setSeater(int(input("How many seater you want : ")))
            print("____________________________________")
            Carss.addCars(ob)
        elif ch2==4:
            Cars=Carss.displayCars()
            for item in Cars:
                print(f"{item.getCarno()}\t{item.getName()}\t{item.getSeater()}")
    elif ch1==2:
        print("                                                   < CUSTOMER SERVICE >")
        print("_________________________________________________")
        print("Press '5' for Add Customer's : ")
        print("Press '6' for Display Customer's : ")
        print("_________________________________________________")
        ch3=int(input("Enter your choice : "))
        if ch3==5:
            ob1=Customer()
            print("_________________________________________________")
            ob1.setName(input("Enter Customer Name :  "))
            ob1.setContact(int(input("Enter Customer's Contact No. : ")))
            ob1.setCity(input("Enter Customer's City  : "))
            print("_________________________________________________")
            Cuss.addCustomers(ob1)
        elif ch3==6:
            Data=Cuss.displayCustomers()
            print("___________________________________________________________")
            for item in Data:
                print(f"{item.getName()}\t{item.getContact()}\t{item.getCity()}")
            print("___________________________________________________________")






