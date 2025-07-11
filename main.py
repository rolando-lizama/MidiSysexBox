# main.py
from encoder import RotaryEncoder
from menu import Menu
from display import OLEDMenu
import board
import time

encoder = RotaryEncoder(board.GP14, board.GP15, board.GP13)
menu = Menu(["Start", "Settings", "About", "Exit"])
screen = OLEDMenu()

while True:
    click = encoder.tick()
    pos = encoder.get_position()

    if pos != menu.index:
        if pos > menu.index:
            menu.move_down()
        else:
            menu.move_up()
        screen.update(menu.get_display())

    if click == "single":
        selected = menu.select()
        print(f"Selected: {selected}")

    elif click == "long":
        print("Long press action 🧭")

    elif click == "double":
        print("Double click action ⚡")

    time.sleep(0.05)
