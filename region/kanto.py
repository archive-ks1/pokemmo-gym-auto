try:
    import pydirectinput as pg
    from time import sleep

except ModuleNotFoundError:
    print("Please install pydirectinput library using 'pip install pydirectinput'")

def menu():
    print("Kanto Gyms")
    menu_options = ["Pewter", "Cerulean", "Vermillion (WIP)", "Celadon (WIP)", "Fuchsia (WIP)", "Saffron (WIP)", "Cinnabar (WIP)", "Viridian (Unavailable)", "Back"]

    for i in range(len(menu_options)):
        print("[{}] {}".format(i+1, menu_options[i]))

def initialize(gym):
    print("Selected {} City Gym".format(gym))
    for sec in range(5, 0, -1):
        sleep(1)
        print("Starting Auto in {} sec(s)...".format(sec))
    
    sleep(1)
    print("In Progress...")

def pewter_pathing_in():
    initialize("Pewter")
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
    print("Entering Pewter City Gym...")

def cerulean_pathing_in():
    initialize("Cerulean")
    pg.press('2')
    pg.keyDown('s')
    sleep(0.02)
    pg.keyUp('s')
    pg.keyDown('d')
    sleep(0.62)
    pg.keyUp('d')
    pg.keyDown('w')
    sleep(0.32)
    pg.keyUp('w')
    print("Entering Cerulean City Gym...")

def main():
    menu()
    user_input = int(input('\nEnter option: '))

    if user_input == 1:
        pewter_pathing_in()
    
    elif user_input == 2:
        cerulean_pathing_in()

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
