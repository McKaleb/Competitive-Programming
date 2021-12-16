import sys

# P.S. The emojis included in this program will be visible if you use VS-Code. They may not be visible in the original python IDLE.

print("\n★ Students' Café Menu - AAU® (v1.0) ★\n")

monday = "\nMONDAY'S MENU 🍴\nBreakfast - Firfir with bread and tea\nLunch - Minchet with 1/2 injera and bread or 1 injera or 2 breads\nDinner - Gulash with 1/2 injera and bread or 1 injera or 2 breads\n"
tuesday = monday.replace("\nMONDAY'S MENU 🍴\nBreakfast - Firfir", "\nTUESDAY'S MENU 🍴\nBreakfast - Qinche")
wednesday = "\nWEDNESDAY'S MENU 🍴\nBreakfast - Strawberry jam with bread and tea\nLunch - Misir Wot and Atikilt with 1/2 injera and bread or 1 injera or 2 breads.\nDinner - Kik wot with 1/2 injera and bread or 1 injera or 2 breads\n"
thursday = monday.replace("MONDAY'S MENU", "THURSDAY'S MENU")
friday = wednesday.replace("WEDNESDAY'S", "FRIDAY'S").replace("Misir Wot and Atikilt", "Misir Wot")
saturday = wednesday.replace("WEDNESDAY'S", "SATURDAY'S").replace("Strawberry jam", "Qinche").replace(" and Atikilt", "")
sunday = monday.replace("MONDAY'S MENU 🍴\nBreakfast - Firfir", "SUNDAY'S MENU 🍴\nBreakfast - Boiled egg")
fasting_days = "\x1B[There are also fasting foods (like Misir-Wot) available for those who fast during fasting seasons.]\x1B\n"

is_cafe_user = input('''Hi there👋, Welcome!
This platform is made for AAU students to check the menu of AAU students' café.
In this platform, you can find the meal menu of every weekdays and weekends.
( You can type 'exit' anytime you want ;) )

Are you students' café user at AAU? (yes/no): ''')
if is_cafe_user.lower() == "yes":
    def menu():
        while True:
                days_of_week = input("\nAWESOME!✌️\nWhat day's menu would you like to see?\n(Enter the name of the day of the week, e.g Monday): \n➤  ")
                if days_of_week.capitalize() == "Monday":
                    print(monday + fasting_days)
                    break
                elif days_of_week.capitalize() == "Tuesday":
                    print(tuesday + fasting_days)
                    break
                elif days_of_week.capitalize() == "Wednesday":
                    print(wednesday)
                    break
                elif days_of_week.capitalize() == "Thursday":
                    print(thursday + fasting_days)
                    break
                elif days_of_week.capitalize() == "Friday":
                    print(friday)
                    break
                elif days_of_week.capitalize() == "Saturday":
                    print(saturday)
                    break
                elif days_of_week.capitalize() == "Sunday":
                    print(sunday + fasting_days)
                    break
                elif days_of_week.lower() == "exit":
                    sys.exit()
                else:
                    print("\n⚠ ⚠ ⚠  Wrong input. Please try again!  ⚠ ⚠ ⚠")
                    menu()
                    break
                return
    menu()
    def tryAgain():
        while True:
            try_again = input("[Would you like to use this program again? ↺ (YES/NO)]: ")
            if try_again.lower() == 'yes':
                menu()
            elif try_again.lower() == 'no':
                print("\nThanks for using this program. \nDon't Have a Good Day, Have a Great Day! 😁\n")
                break
            elif try_again == "exit":
                sys.exit()
            else: 
                print("\n⚠ ⚠ ⚠  Wrong input  ⚠ ⚠ ⚠\n")  
                tryAgain()                  
                break
    tryAgain()
elif is_cafe_user.lower() == 'no':
    print("\nSorry, this platform is for cafe users only.😔 \nAlthough you can get meals for a cheap price from the students' lounges in this college. \n\nHave a good day!✌\n")
elif is_cafe_user == "exit":
    sys.exit()
else:
    print("\n⚠ ⚠ ⚠  Wrong input! Run the program again.  ⚠ ⚠ ⚠\n")

