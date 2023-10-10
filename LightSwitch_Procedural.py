#Procedural light switch

def turn_on():
    global switch_is_on
    #turn the light on
    switch_is_on = True

def turn_off():
    global switch_is_on
    # turn the light off
    switch_is_on = False

# Main code
switch_is_on = False # a global Boolean Value

# Test code
print(switch_is_on)
turn_on()
print(switch_is_on)
turn_off()
print(switch_is_on)
turn_on()
print(switch_is_on)

## Object Oriented Switch
class LightSwitch():
    def __init__(self):
        self.switch_is_on = False

    def turn_on(self):
        # turn the switch on 
        self.switch_is_on = True

    def turn_off(self):
        # turn the switch off
        self.switch_is_on = False

oLightSwitch = LightSwitch()