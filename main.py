from characters import Character
from characters import mockGPIO
#from RPIO import PWM
import time

#PWM.setup()
#PWM.init_channel(4)             # read about DMA channels
#PWM.clear_channel_gpio(0, 17)   # physical pin 11

GPIO_PIN = [17, 18, 19, 20, 21]  # pin numbers corresponding to 15660
DMA_CHANNEL = 4

address = [Character(place) for place in range (0, 5)]

def updateLED(speed):            # transition speed in seconds
    update_count = 0
    while update_count < 5:
        update_count = 0
        for i in range(0, 5):
            address[i].update()
            for j in range (0, 3):
                width = int(address[i].color[j] * (19999 / 255) * (address[i].brightness / 100))
                #PWM.add_channel_pulse(DMA_CHANNEL, GPIO_PIN[i], 0, width)
                mockGPIO(DMA_CHANNEL, GPIO_PIN[i], 0, width)

            if address[i].updating == False:
                update_count += 1

            time.sleep(speed)

# address[1].adjustBrightness(100)
address[2].adjustColor([100,100,100])

while True:
    updateLED(0.005)
    address[2].adjustBrightness(50)
    updateLED(0.05)

