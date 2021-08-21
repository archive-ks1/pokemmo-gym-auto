def menu():
    print("Select your Region")
    menu_options = ["Kanto (WIP)", "Hoenn (Unavailable)", "Sinnoh (Unavailable)", "Unova (Unavailable)", "Exit"]

    for i in range(len(menu_options)):
        print("[{}] {}".format(i+1, menu_options[i]))

while True:
    try:
        print("Welcome to PokeMMO Gym Farming Automation\n")
        menu()
        user_input = int(input('\nEnter option: '))

        if user_input == 1:
            print("Listing Kanto Gym options...\n")
            import region.kanto as kanto
            kanto.main()

        elif user_input == 2:
            print("Hoenn Gyms are not available yet.\n")

        elif user_input == 3:
            print("Sinnoh Gyms are not available yet.\n")

        elif user_input == 4:
            print("Unova Gyms are not available yet.\n")

        elif user_input == 5:
            print("Exiting...\n")
            break
        
    except:
        print('Invalid Input\n')
