from tours import show_tours
from car_rental import show_cars, rent_car, viw_car_rentals
from booking import book_tours, view_bookings, search_booking, cancel_booking
from config import company_name, company_type


def main():
    while True:
       print("==================")
       print("  ",company_name)
       print("  ",company_type)
   
       print("==================")

       print("1. View Tour Pacakages")
       print("2. Book a Tour")
       print("3. View Car Rental Options")
       print("4. View Bookings")
       print("5. Search Bookings")
       print("6. Cancel Booking")
       print("7. View Car Rentals Records")
       print("8. Exit")

       choice=input("Enter your choice:")

       if choice=="1":
          show_tours()
       elif choice=="2":
          book_tours()    
       elif choice=="3":
          rent_car()
       elif choice=="4":
          view_bookings()
       elif choice=="5":
          search_booking()
       elif choice=="6":
          cancel_booking()
       elif choice=="7":
          viw_car_rentals()
       elif choice=="8":
          print("Thank you for using Manasi Tours and Travels")
          break
       else:
        print("Invalid Choice.")


main()