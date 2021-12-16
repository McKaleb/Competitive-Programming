
# Name - Kaleb Mathewos
# ID - UGR/6298/13
# Section - 1
# College - AAiT
# Department - Pre-engineering
# GitHub - @McKaleb

print("\n[Students' Café Menu - AAU (v1.0)]\n")

monday = "\nMONDAY'S MENU\nBreakfast - Firfir with bread and tea\nLunch - Minchet with 1/2 injera and bread or 1 injera or 2 breads\nDinner - Gulash with 1/2 injera and bread or 1 injera or 2 breads\n"
tuesday = monday.replace("\nMONDAY'S MENU\nBreakfast - Firfir with bread and tea\n", "\nTUESDAY'S MENU\nBreakfast - Qinche with bread and tea\n")
wednesday = "\nWEDNESDAY'S MENU\nBreakfast - Strawberry jam with bread and tea\nLunch - Misir Wot and Atikilt with 1/2 injera and bread or 1 injera or 2 breads.\nDinner - Kik wot with 1/2 injera and bread or 1 injera or 2 breads\n"
thursday = monday.replace("MONDAY'S MENU", "THURSDAY'S MENU")
friday = wednesday.replace("WEDNESDAY'S", "FRIDAY'S").replace("Misir Wot and Atikilt", "Misir Wot")
saturday = wednesday.replace("WEDNESDAY'S", "SATURDAY'S").replace("Strawberry jam", "Qinche").replace(" and Atikilt", "")
sunday = monday.replace("MONDAY'S MENU\nBreakfast - Firfir", "SUNDAY'S MENU\nBreakfast - Boiled egg")

is_cafe_user = input('''Hi there, Welcome!
This platform is made for AAU students to check the menu schedules of AAU's students' café.
Here, you can find the meal schedules of every weekdays and weekends.
(You can type 'exit' anytime you want :))

Are you students' café user at AAU? (yes/no): ''')
if is_cafe_user.lower() == "yes":
    def menu():
        runprogram = True
        while runprogram:
                days_of_week = input("\nAWESOME!\nWhat day's Menu would you like to see?\n(Enter the name of the day of the week, e.g Monday): \n>> ")
                if days_of_week.capitalize() == "Monday":
                    print(monday)
                    break
                elif days_of_week.capitalize() == "Tuesday":
                    print(tuesday)
                    break
                elif days_of_week.capitalize() == "Wednesday":
                    print(wednesday)
                    break
                elif days_of_week.capitalize() == "Thursday":
                    print(thursday)
                    break
                elif days_of_week.capitalize() == "Friday":
                    print(friday)
                    break
                elif days_of_week.capitalize() == "Saturday":
                    print(saturday)
                    break
                elif days_of_week.capitalize() == "Sunday":
                    print(sunday)
                    break
                elif days_of_week.lower() == "exit":
                    runprogram = False
                else:
                    print("\nWrong input. Please try again!\n")
                return
    menu()
    def tryAgain():
        reuse = True
        while reuse:
            try_again = input("[Would you like to use this program again? (YES/NO)]: ")
            if try_again.lower() == 'yes':
                menu()
            elif try_again.lower() == 'no':
                print("\nThanks for using this program. Have a nice day!")
                break
            elif try_again == "exit":
                reuse = False
            else: 
                print("\nWrong input\n")  
                tryAgain()                  
                break
    tryAgain()
elif is_cafe_user.lower() == 'no':
    print("\nSorry, this platform is for cafe users only. \nAlthough you can get meals for a cheap price from the students' lounges in this college. \n\nHave a good day!\n")
elif is_cafe_user == "exit":
    None
else:
    print("\nWrong input! Run the program again.\n")

