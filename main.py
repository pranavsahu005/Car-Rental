from Entity.Car import Car
from Entity.Customer import Customer
from Service.CarService import CarService
from Service.CustomerService import CustomerService
Carss=CarService()
Cuss=CustomerService()
while True:
    print("                                                                ")
    print( " *************** <WEAR TOME RENTAL SERVICES> *************** " )
    print("                                                                ")
    print("                      *********< W >*********** ")
    print("                                                                ")
    print("_____________GLOBAL TRANSPORT LIMITED CO.LTD PVT___________________")

    print("_______________________________________________")
    print("Press 1 for CAR SERVICE !! ")
    print("Press 2 for CUSTOMER SERVICE !! ")
    print("______________________________________________")
    ch1=int(input("Enter your choice "))
    if ch1==1:
        print("                                                   < CAR SERVICE >")
        print("                                                                ")
        print("_______________________________________________")
        print("Press 1 for Add  Cars !")
        print("Press 2 for Display Cars !")
        print("Press 3 for Remove Car ! ")
        print("Press 4 for search any Car !")
        print("___________________________________________")
        ch2=int(input("Enter your Choice !! "))
        if ch2==1:
            ob=Car()
            print("_______________________________________")
            ob.setCarno(input("Enter Car number : "))
            ob.setName(input("Enter Car Name :  "))
            ob.setSeater(int(input("How many seater you want : ")))
            print("_______________________________________")
            Carss.addCars(ob)
        elif ch2==2:
            Cars=Carss.displayCars()
            print("\t \t CAR NO \t \t CAR NAME \t \t SEATER")
            for item in Cars:
                print(f"\t \t {item.getCarno()}\t \t{item.getName()} \t \t{item.getSeater()}")
        elif ch2==3:
            Cars=Carss.displayCars()
            i=0
            print("\t \t CAR NO \t \t CAR NAME \t \t SEATER")
            for item in Cars:
                print(f"\t \t {item.getCarno()}\t \t{item.getName()} \t \t{item.getSeater()}")
                i=i+1
            index=int(input("\t Enter index to remove the car - "))
            Carss.removeCar(index)
            print("\t Car removed Successfully !! ")
        elif ch2==4:
            Num=input("Enter Car Number - ")
            info=Carss.searchCar(Num)
            if(info==None):
                print("NO CAR FOUND !! ")
            else:
                print("\t \t CAR NO \t \t CAR NAME \t \t SEATER")
                print(f"\t\t{info.getCarno()}\t\t{info.getName()}\t\t{info.getSeater()}")
        elif ch2==5:
            data=cars.displayCars()
            print("Car NO. \t\t Name \t\t Seater ")
            i=0
            for item in data:
                print(f"\t \t {item.getCarno()}\t \t{item.getName()} \t \t{item.getSeater()}")
                i=i+i
            index=int(input("Enter Car index to update "))
            if index>=0 and index<i:
                Cars=cars.getcarbyIndex(index)
                print("Press 1 for update Car Number : ")
                print("Press 2 for update Car Name : ")
                print("Press 3 for update Car Seater : ")
                key = input("Enter New Car Number ")
                if key==1:
                    Cars.setCarno(input("Enter New Car Number: "))
                    cars.updateCar(index,Cars)
                elif key ==2:

                    Cars.setName(input("Enter NEW car Name: "))
                elif key == 3:
                    Cars.setSeater(input("Enter NEW number of car seater: "))
                    cars.updateCar(index,Cars)
                else:
                    print("Invalid Choice: ")
    elif ch1==2:
        print("                                                 < CUSTOMER SERVICE >")
        print("                                                                ")
        print("_________________________________________________")
        print("Press '1' for Add Customer's : ")
        print("Press '2' for Display Customer's : ")
        print("Press '3' for Remove any Customer ! ")
        print("Press '4' for search a Customer !")
        print("_________________________________________________")
        ch3=int(input("Enter your choice : "))
        if ch3==1:
            ob1=Customer()
            print("_________________________________________________")
            ob1.setName(input("Enter Customer Name :  "))
            ob1.setContact(int(input("Enter Customer's Contact No. : ")))
            ob1.setCity(input("Enter Customer's City  : "))
            print("_________________________________________________")
            Cuss.addCustomers(ob1)
        elif ch3==2:
            Data=Cuss.displayCustomers()
            print("___________________________________________________________")
            print("                                                                ")
            print("\t \t NAME \t \t CONTACT \t \t CITY")
            for item in Data:
                print(f"\t\t{item.getName}\t\t{item.getContact()}\t\t{item.getCity()}")
            print("                                                                ")
            print("___________________________________________________________")
        elif ch3 == 3:
            Customers = Cuss.displayCustomers()
            i = 0
            print("\t \t NAME \t \t CONTACT \t \t CITY")
            for item in Customers:
                print(f"\t\t{i}\t{item.getName}\t\t{item.getContact()}\t\t{item.getCity()}")
                i = i + 1
            index = int(input("\t Enter index to remove the customer - "))
            Cuss.removeCustomer(index)
            print("\t Customer removed Successfully !! ")
        elif ch3 == 4:
            Name = input("Enter Customer Name - ")
            info = Cuss.searchCustomer(Name)
            if (info == None):
                print("NO CUSTOMER FOUND !! ")
            else:
                print("\t \t NAME \t \t CONTACT \t \t CITY")
                print(f"\t\t{info.getName}\t\t{info.getContact()}\t\t{info.getCity()}")
