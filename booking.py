#Code given below does the booking part.
from tours import tours,show_tours

bookings=[]



def book_tours():
    print("\n======CUSTOMER DETAILS======")

    name=input("Enter customer name:")
    mobile=input("Enter mobile number:")

    print("\n======SELECT TOUR======")
    show_tours()

    choice=int(input("Enter tour choice:"))

    if choice>=1 and choice<=len(tours):

        people=int(input("Enter number of people:"))

        if people>0:
            tour_name=tours[choice-1][0]
            days=tours[choice-1][1]
            price=tours[choice-1][2]

            total_amount=price*people
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
                  

            booking= [
                name,
                mobile,
                tour_name,
                days,
                people,
                total_amount,
                payment_method
            ]

            bookings.append(booking)

            print("\n========Booking Details========")
            print("Customer Name:",name)
            print("Mobile Number:",mobile)
            print("Tour:",tour_name)
            print("Duration:",days,"days")
            print("Number of people:",people)
            print("Total amount:Rs.",total_amount)
            print("Tour booked successfully!")

        else:
            print("Number of people must be greater than zero.")

    else:
        print("Invalid tour choice.")


def view_bookings():
    print("/n======ALL BOOKINGS======")

    if len(bookings)==0:
        print("No Bookings available.")

    else:
        for i in range(len(bookings)):
            print("\nBooking",i+1)
            print("Customer name:",bookings[i][0])
            print("Mobile number:",bookings[i][1])
            print("Tour:",bookings[i][2])
            print("Duration:",bookings[i][3],"days")
            print("Number of people:",bookings[i][4])
            print("Total amount:Rs.",bookings[i][5])
            print("Payment method:",bookings[i][6])

def search_booking():
    print("\n======SEARCH BOOKINGS======")

    mobile=input("Enter customer mobile number:")

    found=False

    for i in range(len(bookings)):
        if bookings[i][1]==mobile:
            print("\nBooking found!")
            print("Customer name:",bookings[i][0])
            print("Mobile number:",bookings[i][1])
            print("Tour:",bookings[i][2])
            print("Duration:",bookings[i][3],"days")
            print("Number of people:",bookings[i][4])
            print("Total amount:Rs.",bookings[i][5])
            print("Payment method:",bookings[i][6])

            found= True

    if found==False:
        print("No booking found with this mobile number.")


def cancel_booking():
    print("\n======CANCEL BOOKING======")

    mobile=input("Enter customer mobile number:")

    found=False

    for i in range (len(bookings)):

        if bookings[i][1]==mobile:
            print("\nBooking found!")
            print("Customer name:",bookings[i][0])
            print("Tour:",bookings[i][2])
            print("Duration:",bookings[i][3],"days")
            print("Number of people",bookings[i][4])
            print("Total amount:RS.",bookings[i][5])
            print("Payment method:",bookings[i][6])

            confirm=input("Do you wnat to cancel this booking? (yes/no):")

            if confirm=="yes":
                del bookings[i]
                print("Booking cancelled successfully.")
            else:
                print("Booking was not cancelled.")

            found=True
            break
        if found==False:
            print("No booking found with this mobile number.")



            


