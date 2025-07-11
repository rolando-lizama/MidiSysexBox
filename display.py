# display.py
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_ssd1306
import busio
from board import GP17, GP16  # Adjust if needed

class OLEDMenu:
    def __init__(self):
        self.i2c = busio.I2C(GP17, GP16)
        self.display = adafruit_ssd1306.SSD1306_I2C(128, 64, self.i2c)
        self.display.fill(0)
        self.display.show()

    def update(self, lines):
        self.display.fill(0)
        for i, line in enumerate(lines[:5]):
            text_area = label.Label(terminalio.FONT, text=line, x=0, y=10 + i * 12)
            self.display.show(text_area)
        self.display.show()
