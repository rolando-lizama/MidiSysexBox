# encoder.py
import time
import digitalio
import board

class RotaryEncoder:
    def __init__(self, pin_a, pin_b, button_pin):
        self.pin_a = digitalio.DigitalInOut(pin_a)
        self.pin_a.direction = digitalio.Direction.INPUT
        self.pin_a.pull = digitalio.Pull.UP

        self.pin_b = digitalio.DigitalInOut(pin_b)
        self.pin_b.direction = digitalio.Direction.INPUT
        self.pin_b.pull = digitalio.Pull.UP

        self.button = digitalio.DigitalInOut(button_pin)
        self.button.direction = digitalio.Direction.INPUT
        self.button.pull = digitalio.Pull.UP

        self.last_a = self.pin_a.value
        self.position = 0
        self.button_state = self.button.value
        self.last_press_time = 0
        self.last_release_time = 0
        self.click_count = 0

    def tick(self):
        # Rotation
        current_a = self.pin_a.value
        if current_a != self.last_a:
            if self.pin_b.value != current_a:
                self.position += 1
            else:
                self.position -= 1
        self.last_a = current_a

        # Button
        current_button = self.button.value
        now = time.monotonic()
        click_type = None

        if self.button_state and not current_button:
            self.last_press_time = now
        elif not self.button_state and current_button:
            duration = now - self.last_press_time
            if duration > 1.0:
                click_type = "long"
            else:
                self.click_count += 1
                self.last_release_time = now

        if self.click_count == 2 and (now - self.last_release_time) < 0.5:
            click_type = "double"
            self.click_count = 0
        elif self.click_count == 1 and (now - self.last_release_time) > 0.5:
            click_type = "single"
            self.click_count = 0

        self.button_state = current_button
        return click_type

    def get_position(self):
        return self.position
