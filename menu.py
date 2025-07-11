# menu.py
class Menu:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def move_up(self):
        self.index = (self.index - 1) % len(self.items)

    def move_down(self):
        self.index = (self.index + 1) % len(self.items)

    def select(self):
        return self.items[self.index]

    def get_display(self):
        return [f"> {item}" if i == self.index else f"  {item}" for i, item in enumerate(self.items)]
