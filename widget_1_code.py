# Import libraries needed for blinking the LED
import board
import digitalio

# Configure the internal GPIO connected to the LED as a digital output
ledred = digitalio.DigitalInOut(board.GP6)
ledred.direction = digitalio.Direction.OUTPUT
ledblue = digitalio.DigitalInOut(board.GP4)
ledblue.direction = digitalio.Direction.OUTPUT
ledwhite = digitalio.DigitalInOut(board.GP28)
ledwhite.direction = digitalio.Direction.OUTPUT

# Configure the internal GPIO connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set the internal resistor to pull-up

# Print a message on the serial console
print('Hello there! My LED is controlled by the button.')

# State 1: All Off
def state1():
    ledred.value = False
    ledblue.value = False
    ledwhite.value = False

# State 2: Red and Blue LED on
def state2():
    ledred.value = True
    ledblue.value = True
    ledwhite.value = False

# State 3: All on 
def state3():
    ledred.value = True
    ledblue.value = True
    ledwhite.value = True

# Main Block of code
state = 0
holding = False

# Loop so the code runs continuously
while True:
    # Display appropriate colouring scheme
    if state == 0:
        state1()
    elif state == 1:
        state2()
    else:
        state3()

    # Update holding depending on button press
    if not button.value == True: # Button is in "press" mode
        if holding: # If we are in process of pressing the button, don't change state, it means we haven't released yet
            holding = holding
        else:
            state = (state+1)%3 # If we let go of button, we have officially pressed it, so change state
            holding = True
    else: # Button is "not pressed" mode
        holding = False

