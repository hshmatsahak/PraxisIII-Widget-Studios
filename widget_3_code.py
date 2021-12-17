# Import libraries needed for blinking the LED
import board
import digitalio
from digitalio import DigitalInOut, Direction

# Configure the internal GPIO connected to the LED as a digital output

ledred = digitalio.DigitalInOut(board.GP6)
ledred.direction = digitalio.Direction.OUTPUT
ledblue = digitalio.DigitalInOut(board.GP4)
ledblue.direction = digitalio.Direction.OUTPUT
ledwhite = digitalio.DigitalInOut(board.GP28)
ledwhite.direction = digitalio.Direction.OUTPUT


# Setup digital input for PIR sensor:
pir = digitalio.DigitalInOut(board.GP1)
pir.direction = digitalio.Direction.INPUT


# Configure the internal GPIO connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set the internal resistor to pull-up

# Print a message on the serial console
print('Hello there! My LED is controlled by the button.')

def state1():
    ledred.value = False
    ledblue.value = False
    ledwhite.value = False

def state2():
    ledred.value = True
    ledblue.value = True
    ledwhite.value = False

def state3():
    ledred.value = True
    ledblue.value = True
    ledwhite.value = True

state = 0
holding = False
# Loop so the code runs continuously
while True:
    if state == 0:
        state1()
    else:
        if pir.value:
            state3()
        else:
                state2()

    if not button.value == True:
        if holding:
            holding = holding
        else:
            state = (state+1)%2
            holding = True
    else:
        holding = False

