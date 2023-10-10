# Dimmer Switch with Test Code

class DimmerSwitch():
    def __init__(self):
        self.switch_is_on = False
        self.brightness = 0

    def turn_on(self):
        self.switch_is_on = True

    def turn_off(self):
        self.switch_is_on = False

    def raise_level(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lower_level(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Extra method for debugging
    def show(self):
        print("Switch is on?", self.switch_is_on)
        print("Brightness is:", self.brightness)

# Main code 
oDimmer = DimmerSwitch()

# Turn switch on, and raise the level 5 times
oDimmer.turn_on()
oDimmer.raise_level()
oDimmer.raise_level()
oDimmer.raise_level()
oDimmer.raise_level()
oDimmer.raise_level()
oDimmer.show()

# Lower the level 2 times, and turn switch off
oDimmer.lower_level()
oDimmer.lower_level()
oDimmer.turn_off()
oDimmer.show()

# Turn switch on, and raise the level 3 times
oDimmer.turn_on()
oDimmer.raise_level()
oDimmer.raise_level()
oDimmer.raise_level()
oDimmer.show()
