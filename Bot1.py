from pynput.keyboard import Controller, KeyCode, Listener, Key
from pynput.mouse import Button
from pynput.mouse import Controller as mouse_controller
import time

rotation = False
rotation_single = False
running = True

keyboard = Controller()
mouse = mouse_controller()


def on_press(key):
    global running
    global rotation
    global rotation_single

    #print (key)
    if key == KeyCode.from_vk(106): # if * was pressed
        print ("Switched")
        rotation_single = False
        rotation = not rotation
    elif key == Key.shift_r:
        print ("Switched")
        rotation = False
        rotation_single = not rotation_single
    elif key == KeyCode.from_vk(107):  # if + was pressed
        running = False

def on_release(key):
    pass



def main():
    global running
    global rotation
    global rotation_single

    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()

    while running:
        if rotation:
            keyboard.press('3')
            keyboard.release('3')
            time.sleep(1.25)
            mouse.click(Button.left, 1)
            time.sleep(0.5)
            keyboard.press('2')
            keyboard.release('2')
            time.sleep(1)
            mouse.click(Button.right, 1)
            time.sleep(0.5)
            keyboard.press('3')
            keyboard.release('3')
            time.sleep(1.25)
            mouse.click(Button.left, 1)
            time.sleep(0.5)
            keyboard.press('4')
            keyboard.release('4')
            time.sleep(0.5)
            mouse.click(Button.left, 1)
            time.sleep(1.25)
            mouse.click(Button.left, 1)
            time.sleep(0.5)

        elif rotation_single:

            keyboard.press('3')
            keyboard.release('3')
            time.sleep(0.5)
            mouse.click(Button.right, 1)
            time.sleep(1)
            mouse.click(Button.right, 1)
            time.sleep(0.5)
            keyboard.press('2')
            keyboard.release('2')
            time.sleep(0.5)
            mouse.press(Button.left)
            time.sleep(0.5)
            mouse.release(Button.left)
            time.sleep(0.5)




    #listener.join()
    print ("oh")
if __name__ == "__main__":
    main()

