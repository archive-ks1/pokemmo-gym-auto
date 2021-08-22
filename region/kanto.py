try:
    import pydirectinput as pg
    from time import sleep

except ModuleNotFoundError:
    print("Please install pydirectinput library using 'pip install pydirectinput'")

def menu():
    print("Select your Kanto Gym")
    menu_options = ["Pewter", "Cerulean", "Vermillion", "Celadon", "Fuchsia", "Saffron", "Cinnabar", "Viridian (Unavailable)", "Back"]

    for i in range(len(menu_options)):
        print("[{}] {}".format(i+1, menu_options[i]))

def initialize(gym):
    print("Selected {} City Gym".format(gym))
    for sec in range(5, 0, -1):
        sleep(1)
        print("Starting Auto in {} sec(s)...".format(sec))
    
    sleep(1)
    print("In Progress...")

def cut_tree():
    for i in range(5):
        pg.press('e')
        sleep(0.25)
    
    sleep(0.4)

def pewter_pathing_in():
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
    sleep(0.4)
    pg.keyUp('s')
    pg.keyDown('d')
    sleep(0.54)
    pg.keyUp('d')
    pg.keyDown('w')
    sleep(0.2)
    pg.keyUp('w')
    print("Entering Pewter City Gym...")

def approach_brock():
    pg.keyDown('w')
    sleep(1.4)
    pg.keyUp('w')

def cerulean_pathing_in():
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

def vermillion_pathing_in():
    pg.keyDown('d')
    sleep(1)
    pg.keyUp('d')
    pg.keyDown('s')
    sleep(0.5)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(0.3)
    pg.keyUp('a')
    pg.keyDown('s')
    sleep(0.56)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(0.364)
    pg.keyUp('a')
    pg.keyDown('s')
    sleep(0.1)
    pg.keyUp('s')
    cut_tree()
    pg.keyDown('s')
    sleep(0.4)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(0.302)
    pg.keyUp('a')
    pg.keyDown('w')
    sleep(0.2)
    pg.keyUp('w')
    print("Entering Vermillion City Gym...")

def celadon_pathing_in():
    pg.keyDown('s')
    sleep(0.12)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(0.45)
    pg.keyUp('a')
    pg.keyDown('s')
    sleep(0.6)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(0.74)
    pg.keyUp('a')
    pg.keyDown('s')
    sleep(0.7)
    pg.keyUp('s')
    pg.keyDown('d')
    sleep(0.65)
    pg.keyUp('d')
    pg.keyDown('s')
    sleep(0.2)
    pg.keyUp('s')
    cut_tree()
    pg.keyDown('s')
    sleep(0.4)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(2.2)
    pg.keyUp('a')
    pg.keyDown('w')
    sleep(1)
    pg.keyUp('w')
    print("Entering Celadon City Gym...")

def fuchsia_pathing_in():
    pg.press('s')
    pg.keyDown('a')
    sleep(1.2)
    pg.keyUp('a')
    pg.keyDown('w')
    sleep(0.4)
    pg.keyUp('w')
    print("Entering Fuchsia City Gym...")

def saffron_pathing_in():
    pg.press('s')
    pg.keyDown('d')
    sleep(2)
    pg.keyUp('d')
    pg.keyDown('w')
    sleep(1.96)
    pg.keyUp('w')
    pg.keyDown('a')
    sleep(0.345)
    pg.keyUp('a')
    pg.keyDown('w')
    sleep(0.4)
    pg.keyUp('w')
    print("Entering Saffron City Gym...")

def cinnabar_pathing_in():
    pg.keyDown('d')
    sleep(0.5)
    pg.keyUp('d')
    pg.keyDown('w')
    sleep(0.6)
    pg.keyUp('w')
    pg.press('a')
    pg.keyDown('w')
    sleep(0.3)
    pg.keyUp('w')
    print("Entering Cinnabar City Gym...")

def main():
    menu()
    user_input = int(input('\nEnter option: '))

    if user_input == 1:
        initialize("Pewter")
        pg.press('2')
        pewter_pathing_in()
        sleep(1)
        pg.press('shift')
        approach_brock()
    
    elif user_input == 2:
        initialize("Cerulean")
        pg.press('2')
        cerulean_pathing_in()

    elif user_input == 3:
        initialize("Vermillion")
        pg.press('2')
        vermillion_pathing_in()

    elif user_input == 4:
        initialize("Celadon")
        pg.press('2')
        celadon_pathing_in()

    elif user_input == 5:
        initialize("Fuchsia")
        pg.press('2')
        fuchsia_pathing_in()

    elif user_input == 6:
        initialize("Saffron")
        pg.press('2')
        saffron_pathing_in()

    elif user_input == 7:
        initialize("Cinnabar")
        pg.press('2')
        cinnabar_pathing_in()

    elif user_input == 8:
        print("Viridian City Gym is currently not scripted in PokeMMO")

    elif user_input == 9:
        return
