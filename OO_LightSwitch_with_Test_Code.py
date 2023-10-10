## OO_LightSwitch

class LightSwitch():
    def __init__(self):
        self.switch_is_on = False

    def turn_on(self):
        self.switch_is_on = True
    
    def turn_off(self):
        self.switch_is_on = False

    def show(self): # added for testing
        print(self.switch_is_on)

# Main code 
oLightSwitch = LightSwitch()

# Calls to the methods
oLightSwitch.show()
oLightSwitch.turn_on()
oLightSwitch.show()
oLightSwitch.turn_off()
oLightSwitch.show()
oLightSwitch.turn_on()
oLightSwitch.show()

