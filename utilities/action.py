try:
    import pydirectinput as di
    from time import sleep

except ModuleNotFoundError:
    print("Please install pydirectinput library using 'pip install pydirectinput'")

def initialize(gym):
    print("Selected {} City Gym".format(gym))
    for sec in range(5, 0, -1):
        sleep(1)
        print("Starting Auto in {} sec(s)...".format(sec))
    
    sleep(1)
    print("In Progress...")

def cut_tree():
    for i in range(5):
        di.press('e')
        sleep(0.25)
    
    sleep(0.6)

def goto(x, y):
    di.press('1')
    sleep(0.25)
    di.moveTo(x, y, duration = 0.25)
    di.click()
    sleep(5.5)
