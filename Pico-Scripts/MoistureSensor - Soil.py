from machine import Pin, ADC
import time

# LED on pico
LED = Pin("LED", value=0)

# Button inputs on board
buttonon = Pin(14, Pin.IN)
buttontoggle = Pin(15, Pin.IN)

# Power outputs on board
humidpower = Pin(27, Pin.OUT, value=1)
pumppower = Pin(22, Pin.OUT, value=0)

# Values for humidity calculation and sensor sensitivity (Sensor ADC outputs in air and water)
air = 30000
water = 14500
sensitivity = 45 # Humidity percentage that the pump below at

# Designates GPIO 26 as an ADC pin
adc = ADC(26)

# Class for toggling the pump
class Toggle:
    def __init__(self): # Initializes state to True (system off by default)
        self.state = False
    def flip(self):
        self.state = not self.state # Toggles state
        LED.value(not LED.value()) # Toggles LED on pico
        time.sleep_ms(500) # Sleeps to prevent rapid switching

def readhumid(): # Calculates humidity from sensor
    read = adc.read_u16() # Reads the ADC value of GPIO 26
    humidity = 100-(100*((read-water)/(air-water))) # Calculates the humidity % using the values previously defined
    if (humidity > 100): # If the percentage goes above 100%, caps it at 100%
        humidity = 100
    print(humidity) # Prints the humidity to the terminal
    return humidity # Returns the humidity percentage

def toggler(toggle): # Checks if the toggle switch has been activated
    if (buttontoggle.value()): # Detects if the toggle switch is being pressed and toggles the LED and toggle.state
        toggle.flip()   
    return toggle.state # Returns the bool value of toggle.state

def logic(toggle, humidity): # Runs the logic for determining when to run the pump
    if (buttonon.value()): # If manual override is pressed, run pump
        pumppower.value(1)
    elif (humidity < sensitivity and toggle): # If toggle is true and humidity is less than sensitivity, run pump
        pumppower.value(1)
    else: # Else, pump is off
        pumppower.value(0)

def main():
    toggle = Toggle() # Creates an object from the Toggle class
    while (True): # Loops the main part of the script
        time.sleep_ms(100) # Timer controls how often script runs
        logic(toggler(toggle), readhumid()) # Runs the logic for the pump, with the value of toggle.state and the humidity percentage

while __name__ == "__main__": main()