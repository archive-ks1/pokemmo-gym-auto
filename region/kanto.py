try:
    import pydirectinput as pg
    from time import sleep

except ModuleNotFoundError:
    print("Please install pydirectinput library using 'pip install pydirectinput'")

def menu():
    print("Kanto Gyms")
    menu_options = ["Pewter", "Cerulean (WIP)", "Vermillion (WIP)", "Celadon (WIP)", "Fuchsia (WIP)", "Saffron (WIP)", "Cinnabar (WIP)", "Viridian (Unavailable)", "Back"]

    for i in range(len(menu_options)):
        print("[{}] {}".format(i+1, menu_options[i]))

def initialize(gym):
    print("Selected {} City Gym".format(gym))
    for sec in range(5, 0, -1):
        sleep(1)
        print("Starting Auto in {} sec(s)...".format(sec))

    sleep(1)

def pewter_city():
    initialize("Pewter City")
    pg.press('2')
    pg.keyDown('d')
    sleep(0.5)
    pg.keyUp('d')
    pg.keyDown('w')
    sleep(1.1)
    pg.keyUp('w')
    pg.keyDown('a')
    sleep(1.25)
    pg.keyUp('a')
    pg.keyDown('s')
    sleep(0.6)
    pg.keyUp('s')
    pg.keyDown('d')
    sleep(0.54)
    pg.keyUp('d')
    pg.keyDown('w')
    sleep(0.2)
    pg.keyUp('w')

def main():
    menu()
    user_input = int(input('\nEnter option: '))

    if user_input == 1:
        pewter_city()
    
    elif user_input == 2:
        print("Unavailable")

    elif user_input == 3:
        print("Unavailable")

    elif user_input == 4:
        print("Unavailable")

    elif user_input == 5:
        print("Unavailable")

    elif user_input == 6:
        print("Unavailable")

    elif user_input == 7:
        print("Unavailable")

    elif user_input == 8:
        print("Unavailable")

    elif user_input == 9:
        return
