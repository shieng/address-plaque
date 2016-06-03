class Character:

    def __init__(self, number):
        self.updating = False               # is true when setpoints haven't been reached
        self.number = number                # place in address, 0 - 4
        self.color = [255, 255, 255]        # current color, [r, g, b]
        self.setColor = [255, 255, 255]     # set color, [r, g, b]
        self.brightness = 100.              # brightness, 0 - 100

    def adjustBrightness(self, newBrightness):
        self.brightness = float(newBrightness)

    def adjustColor(self, newColor):
        self.setColor = newColor
        self.updating = True

    def update(self):
        update_count = 0                    # counts updated updated numbers

        for i in range(0, 3):
            #self.color[i] = self.color[i] * self.brightness / 100
            c_diff = self.color[i] - self.setColor[i]
            if c_diff < 0:
                self.color[i] += 1
                print "adding"
            elif c_diff > 0:
                self.color[i] -= 1
                print "subracting"
            else:
                update_count += 1

        for i in range(0, 3):
            if self.color[i] < 0:
                self.color[i] = 0
            elif self.color[i] > 255:
                self.color[i] = 255

        if update_count == 3:
            self.updating = False
        elif update_count > 3:
            print "update_count error"
        else:
            self.updating = True

        print ("count: ", update_count, "    update: ", self.updating)
        
def mockGPIO(dma_channel, gpio_pin, start, width):
    print ("DMA: ", dma_channel, "    PIN: ", gpio_pin, "    START: ", start, "    WIDTH: ", width)

    

