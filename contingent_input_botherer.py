# Python3 Contingent Mouse Mover

import sys
from time import sleep
from datetime import datetime
from pynput.keyboard import Key, Controller as KeyboardController, Listener as KeyboardListener
from pynput.mouse import Controller as MouseController, Listener as MouseListener

# misc vars
intervallength = int (sys.argv[1]) if len(sys.argv) > 1 else 60
verbose = bool (sys.argv[4]) if len(sys.argv) > 4 else False
def maybe_print(*args):
    global verbose
    if (verbose):
        print(datetime.now(), *args)

# mouse-related vars
dx = int (sys.argv[2]) if len(sys.argv) > 2 else 5
dy = int (sys.argv[3]) if len(sys.argv) > 3 else 5
mouseactive = True
scrollcount = 0
mouse = MouseController()
previousposition = mouse.position
multiplier = -1
def mouse_on_move(*args):
    global mouse, mouseactive, previousposition, dx, dy
    maybe_print(*args)
    newmouseactive = bool (max(abs(mouse.position[0] - previousposition[0]), abs(mouse.position[1] - previousposition[1])) >= max(dx, dy))
    if (not mouseactive and newmouseactive):
        maybe_print('mouse_on_move setting mouseactive:', *args)
        mouseactive = newmouseactive
def mouse_on_scroll(*args):
    global mouseactive, scrollcount, dy
    if (not mouseactive):
        scrollcount += 1
        if (scrollcount >= dy):
            maybe_print('mouse_on_scroll setting mouseactive', *args)
            mouseactive = True
def mouse_on_click(*args):
    global mouseactive
    if (not mouseactive):
        maybe_print('mouse_on_click setting mouseactive:', *args)
        mouseactive = True
mouselistener = MouseListener(
    on_scroll=mouse_on_scroll,
    on_move=mouse_on_move,
    on_click=mouse_on_click
)
mouselistener.start()

# key-related vars
keyactive = True
keyboard = KeyboardController()
def on_key(key):
    global keyactive
    # print('{0} detected'.format(key))
    if (not keyactive):
        keyactive = True
keylistener = KeyboardListener(on_press=on_key, on_release=on_key)
keylistener.start()

while (1):
    currentposition = mouse.position
    if (not keyactive and not mouseactive):
        maybe_print("No keyboard activity or significant mouse movement detected: bothering inputs.")
        try:
            # Set activity flags to true to the stuff we're about to do doesn't trigger the listeners.
            keyactive = True
            mouseactive = True

            keyboard.press(Key.cmd)
            keyboard.release(Key.cmd)
            
            sleep(0.5)

            keyboard.press(Key.cmd)
            keyboard.release(Key.cmd)
            
            mouse.move(dx * multiplier, dy * multiplier)
            multiplier *= -1
            sleep(0.01)
        except Exception as e:
            print("Exception:", e)
            exit
    else:
        maybe_print("Keyboard has been used or mouse has moved: not bothering inputs.")
    previousposition = mouse.position
    keyactive = False
    mouseactive = False
    scrollcount = 0
    sleep(intervallength)
