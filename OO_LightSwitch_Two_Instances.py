## OO_LightSwitch
class LightSwitch():
    def __init__(self):
        self.switch_is_on = False

    def turn_on(self):
        self.switch_is_on = False

    def turn_on(self):
        self.switch_is_on = True

    def turn_off(self):
        self.switch_is_on = False

    def show(self):
        print(self.switch_is_on)

# Main code
oLightSwitch1 = LightSwitch() # Create a LightSwitch object
oLightSwitch2 = LightSwitch() # Create another LightSwitch object

# Test Code 
oLightSwitch1.show()
oLightSwitch2.show()
oLightSwitch1.turn_on()# Turn switch 1 on 
# Switch 2 should be off at the start, but this makes it clearer
oLightSwitch2.turn_off()
oLightSwitch1.show()
oLightSwitch2.show()