from RPIO import PWM
import time

PWM.setup()
PWM.init_channel(4) #read about DMA channels

def updateLED(character):
    PWM.add_channel_pulse(

class Character:

    def __init__(self, number, place):
        self.number = number            # actual number, 15660
        self.place = place              # its location, 0 - 4
        self.color = [255, 255, 255]    # current color, [r, g, b]
        self.setColor = [255, 255, 255] # set color, [r, g, b]  
        self.brightness = 255           # current brightness, 0 - 255
        self.setBrightness = 255        # set brightness, 0 - 255

    def adjustBrightness(self, newBrightness):
        self.setBrightness = newBrightness

    def adjustColor(self, newColor):
        self.setColor = newColor 

    def update(self):
        b_diff = self.brightness - self.setBrightness
        if b_diff < 0:
            self.brightness += 1
            for i in range(0,3):
                self.color[i] += 1

        elif b_diff > 0:
            self.brightness -= 1
            for i in range(0,3):
                self.color[i] -= 1

        else:
            # do nothing

        for i in range(0, 3):
            c_diff[i] = self.color[i] - self.setColor[i]
            if c_diff < 0:
                self.color[i] += 1

            elif c_diff > 0:
                self.color[i] -= 1

            else:
                # do nothing

            if self.color[i] < 0:
                self.color[i] = 0

            elif self.color[i] > 255:
                self.color[i] = 255

            else:
                # do nothing

        
one = Character(1, 0)
five = Character(5, 1)
six = Character(6, 2)

print one.setBrightness
one.adjustBrightness(40)
one.adjustColor([100, 100, 100])

for i in range(0, 100):
    one.update()
    PWM.add_channel_pulse(4, 17, 0, one.brightness)
    time.sleep(0.02)

    


    

"""

print "...0, 50)"
PWM.add_channel_pulse(0, 17, 0, 1999)
time.sleep(5)
print "...100, 50)"
PWM.add_channel_pulse(0, 17, 0, 1000)
time.sleep(5)

PWM.clear_channel_gpio(0, 17)
PWM.cleanup()

"""
