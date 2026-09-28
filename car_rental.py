cars=[
    ["Swift Dzire",2500],
    ["Ertiga",3000],
    ["Innova",3500],
    ["Tempo Traveller",4500]
]

car_rental=[]


def show_cars():
    print("\n============CAR RENTAL============")
    for i in range(len(cars)):
        print(i+1,".",cars[i][0])
        print("   Price per day: Rs.",cars[i][1])
        print("-----------------------------------")


def rent_car():
    print("\n====== CAR RENTAL======")

    name=input("Enter customer name:")
    mobile=input("Enter mobile number:")

    show_cars()
    choice=int(input("Enter car choice: "))
    if choice>=1 and choice<=len(cars):
        days=int(input("Enter number of days: "))
        if days>0:
            car_name=cars[choice-1][0]
            price_per_day=cars[choice-1][1]

            total_amount=price_per_day*days


            print("\n======PAYMENT======")
            print("Total amount:Rs.",total_amount)
            print("1.UPI")
            print("2.Cash")
            print("3.Card")

            payment_method=int(input("Enter payment method:"))
            
            if payment_method==1:
                payment_method="UPI"
            elif payment_method==2:
                payment_method="Cash"
            elif payment_method==3:
                payment_method="Card"
            else:
                payment_method="Not selected"

            print("Payment method:",payment_method)
            print("Payment successful!")

            rental= [
                name,
                mobile,
                car_name,
                price_per_day,
                days,
                total_amount,
                payment_method
            ]
            car_rental.append(rental)

            print("\n========Rental Details========")
            print("Customer Name:",name)
            print("Mobile Number:",mobile)
            print("Car:",car_name)
            print("Price per day:Rs.",price_per_day)
            print("Number of days:",days)
            print("Total amount:Rs.",total_amount)
            print("Payment method:",payment_method)
            print("Car rental booked successfully!")

        else:
            print("Number of days must be greater than zero.")
    else:
        print("Invalid car choice.")  


def viw_car_rentals():
    print("\n======ALL RENTALS RECORDS======")

    if len(car_rental)==0:
        print("No Car Rentals available.")

    else:
        for i in range(len(car_rental)):
            print("\nRental",i+1)
            print("Customer name:",car_rental[i][0])
            print("Mobile number:",car_rental[i][1])
            print("Car:",car_rental[i][2])
            print("Price per day:Rs.",car_rental[i][3])
            print("Number of days:",car_rental[i][4])
            print("Total amount:Rs.",car_rental[i][5]) 
            print("Payment method:",car_rental[i][6])         


            