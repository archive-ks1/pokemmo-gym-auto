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
    
    sleep(0.6)

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

def pewter_pathing_out():
    pg.keyDown('s')
    sleep(1.5)
    pg.keyUp('s')

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

def approach_misty():
    pg.press('d')
    pg.keyDown('w')
    sleep(1.3)
    pg.keyUp('w')
    pg.keyDown('d')
    sleep(0.4)
    pg.keyUp('d')
    pg.keyDown('w')
    sleep(0.4)
    pg.keyUp('w')
    pg.keyDown('a')
    sleep(0.6)
    pg.keyUp('a')
    pg.press('w')

def cerulean_pathing_out():
    pg.keyDown('d')
    sleep(0.6)
    pg.keyUp('d')
    pg.keyDown('s')
    sleep(0.6)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(0.4)
    pg.keyUp('a')
    pg.keyDown('s')
    sleep(1.4)
    pg.keyUp('s')
    pg.press('a')
    pg.press('s')

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
    sleep(0.45)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(0.302)
    pg.keyUp('a')
    pg.keyDown('w')
    sleep(0.2)
    pg.keyUp('w')
    print("Entering Vermillion City Gym...")

def approach_surge():
    pg.press('d')
    pg.keyDown('w')
    sleep(3)
    pg.keyUp('w')
    pg.press('a')

def vermillion_pathing_out():
    pg.keyDown('s')
    sleep(3)
    pg.keyUp('s')
    pg.press('a')
    pg.press('s')

def celadon_pathing_in():
    sleep(0.1)
    pg.press('s')
    pg.keyDown('a')
    sleep(0.452)
    pg.keyUp('a')
    pg.keyDown('s')
    sleep(0.74)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(0.791)
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
    sleep(0.345)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(2.23)
    pg.keyUp('a')
    pg.keyDown('w')
    sleep(1)
    pg.keyUp('w')
    print("Entering Celadon City Gym...")

def approach_erika():
    pg.keyDown('w')
    sleep(1.4)
    pg.keyUp('w')
    cut_tree()
    pg.keyDown('w')
    sleep(0.8)
    pg.keyUp('w')

def celadon_pathing_out():
    pg.keyDown('s')
    sleep(2.8)
    pg.keyUp('s')

def fuchsia_pathing_in():
    pg.press('s')
    pg.keyDown('a')
    sleep(1.2)
    pg.keyUp('a')
    pg.keyDown('w')
    sleep(0.4)
    pg.keyUp('w')
    print("Entering Fuchsia City Gym...")

def approach_koga():
    pg.keyDown('d')
    sleep(1.3)
    pg.keyUp('d')
    pg.keyDown('w')
    sleep(3.8)
    pg.keyUp('w')
    pg.keyDown('a')
    sleep(0.8)
    pg.keyUp('a')
    pg.keyDown('s')
    sleep(1.3)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(1.25)
    pg.keyUp('a')
    pg.keyDown('s')
    sleep(0.25)
    pg.keyUp('s')
    pg.keyDown('d')
    sleep(0.85)
    pg.keyUp('d')
    pg.press('s')

def fuchsia_pathing_out():
    pg.keyDown('a')
    sleep(1)
    pg.keyUp('a')
    pg.keyDown('w')
    sleep(0.32)
    pg.keyUp('w')
    pg.keyDown('d')
    sleep(1.35)
    pg.keyUp('d')
    pg.keyDown('w')
    sleep(1.8)
    pg.keyUp('w')
    pg.keyDown('d')
    sleep(1)
    pg.keyUp('d')
    pg.keyDown('s')
    sleep(3.8)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(1.2)
    pg.keyUp('a')
    pg.press('s')

def saffron_pathing_in():
    pg.press('s')
    pg.keyDown('d')
    sleep(2.02)
    pg.keyUp('d')
    pg.keyDown('w')
    sleep(1.96)
    pg.keyUp('w')
    pg.keyDown('a')
    sleep(0.25)
    pg.keyUp('a')
    pg.keyDown('w')
    sleep(0.4)
    pg.keyUp('w')
    print("Entering Saffron City Gym...")

def approach_sabrina():
    pg.keyDown('d')
    sleep(0.8)
    pg.keyUp('d')
    pg.keyDown('w')
    sleep(1)
    pg.keyUp('w')
    pg.keyDown('a')
    sleep(8)
    pg.keyUp('a')
    pg.keyDown('s')
    sleep(1)
    pg.keyUp('s')
    sleep(1)
    pg.keyDown('a')
    sleep(0.6)
    pg.keyUp('a')
    pg.keyDown('w')
    sleep(0.8)
    pg.keyUp('w')

def saffron_pathing_out():
    pg.keyDown('s')
    sleep(0.7)
    pg.keyUp('s')
    pg.keyDown('d')
    sleep(1)
    pg.keyUp('d')
    pg.keyDown('w')
    sleep(1.2)
    pg.keyUp('w')
    pg.keyDown('d')
    sleep(8)
    pg.keyUp('d')
    sleep(1)
    pg.keyDown('s')
    sleep(0.6)
    pg.keyUp('s')
    pg.keyDown('a')
    sleep(0.6)
    pg.keyUp('a')
    pg.keyDown('s')
    sleep(0.2)
    pg.keyUp('s')

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
        # enter combat
        sleep(1)
        pewter_pathing_out()
    
    elif user_input == 2:
        initialize("Cerulean")
        pg.press('2')
        cerulean_pathing_in()
        sleep(1)
        pg.press('shift')
        approach_misty()
        # enter combat
        sleep(1)
        cerulean_pathing_out()

    elif user_input == 3:
        initialize("Vermillion")
        pg.press('2')
        vermillion_pathing_in()
        sleep(1)
        pg.press('shift')
        approach_surge()
        # enter combat
        sleep(1)
        vermillion_pathing_out()

    elif user_input == 4:
        initialize("Celadon")
        pg.press('2')
        celadon_pathing_in()
        sleep(1)
        pg.press('shift')
        approach_erika()
        # enter combat
        sleep(1)
        celadon_pathing_out()

    elif user_input == 5:
        initialize("Fuchsia")
        pg.press('2')
        fuchsia_pathing_in()
        sleep(1)
        pg.press('shift')
        approach_koga()
        # enter combat
        sleep(1)
        fuchsia_pathing_out()

    elif user_input == 6:
        initialize("Saffron")
        pg.press('2')
        saffron_pathing_in()
        sleep(1)
        pg.press('shift')
        approach_sabrina()
        # enter combat
        sleep(1)
        saffron_pathing_out()

    elif user_input == 7:
        initialize("Cinnabar")
        pg.press('2')
        cinnabar_pathing_in()

    elif user_input == 8:
        print("Viridian City Gym is currently not scripted in PokeMMO")

    elif user_input == 9:
        return
