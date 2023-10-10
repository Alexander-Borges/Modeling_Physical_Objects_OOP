# TV Class
class TV():
    def __init__(self):
        self.is_on = False
        self.is_muted = False
        # Some default list of channels
        self.channel_list = [2,4,5,7,9,11,20,36,44,54,65]
        self.n_channels = len(self.channel_list)
        self.channel_index = 0
        self.VOLUME_MINIMUM = 0 # constant
        self.VOLUME_MAXIMUM = 10 # constant
        self.volume = self.VOLUME_MAXIMUM // 2 # integer divide

    def power(self):
        self.is_on = not self.is_on # toggle

    def volume_up(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted = False # changing the volume while muted un-mutes the sound
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volume_down(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted = False # changing the volume while muted un-mutes the sound
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channel_up(self):
        if not self.is_on:
            return
        self.channel_index = self.channel_index + 1
        if self.channel_index > self.n_channels:
            self.channel_index = 0 # wrap around to the first channel

    def channel_down(self):
        if not self.is_on:
            return
        self.channel_index = self.channel_index - 1
        if self.channel_index > self.n_channels:
            self.channel_index = 0 # wrap around to the first channel

    def mute(self):
        if not self.is_on:
            return 
        self.is_muted = not self.is_muted

    def set_channel(self, new_channel):
        if new_channel in self.channel_list:
            self.channel_index = self.channel_list.index(new_channel)

    def show_info(self):
        print()
        print("TV Status:")
        if self.is_on:
            print("     TV is on")
            print("     Channel is:", self.channel_list[self.channel_index])
            if self.is_muted:
                print("     Volume is:", self.volume, "(sound is muted)")
            else:
                print("     Volume is:", self.volume)
        else:
            print("     TV is off")


#   Main code
oTV = TV() # Create the TV Object

#Turn on the TV and show the status
oTV.power()
oTV.show_info()

# Change the channel up twice, raise the volume twice, show status
oTV.channel_up()
oTV.channel_up()
oTV.volume_up()
oTV.volume_up()
oTV.show_info()

# Turn the TV off, show status, turn the TV on, show status
oTV.power()
oTV.show_info()
oTV.power()
oTV.show_info()