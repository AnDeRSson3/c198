
while True:
    Total=0
    
    while True:
        Customer_name = input("Customer Name?: ")
        Quantity=float(input("Enter the quantity of items: "))
        Price=float(input("Enter the price of items: "))
        Total=round(Quantity*Price,2)
        Repeat= input("Do you want to repeat this process(Y/N)?")
        if Repeat=="N" or Repeat=="n":
            print("_"*50)
            print("Name: ", Customer_name)
            print("Total Cost: $",Total)
            print()
            print("*****Thank you for shopping with us*****")
            print("_"*50)
            New_Customer=input("Go to next person(Y/N)?")
            if New_Customer=='n' or New_Customer=="N":
                break
            