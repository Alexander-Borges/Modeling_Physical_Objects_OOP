# DimmerSwitch Class
class DimmerSwitch():
    def __init__(self):
        self.switch_is_on = False
        self.brightness = 0

    def turn_on(self):
        self.switch_is_on = True

    def turn_off(self):
        self.switch_is_on = False

    def raise_level(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Extra method for debugging
    def show(self):
        print("Switch is on?", self.switch_is_on)
        print("Brightness is:", self.brightness)