from machine import Pin, ADC, PWM
import time

# LED
green = Pin(11, Pin.OUT, value=0)
blue = PWM(Pin(12), freq=2000, duty_u16=0)
red = PWM(Pin(13), freq=2000, duty_u16=0)

# Rotary Encoder
rotaryA = Pin(16, Pin.IN)
rotaryB = Pin(17, Pin.IN)

# Switch Inputs
on = Pin(15, Pin.IN, Pin.PULL_DOWN)
off = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Power outputs on board
pumppower = Pin(22, Pin.OUT, value=0)

# Values for humidity calculation and sensor sensitivity (Sensor ADC outputs in air and water)
air = 30000
water = 14500
sensitivity = [45] # Humidity percentage that the pump below at

# Designates GPIO 26 as an ADC pin
adc = ADC(26)

def setsensitivity(): # Adjusts the sensitivity based on the rotary encoder
    lastA = rotaryA.value()
    time.sleep_ms(5)
    if (lastA != rotaryA.value()): # Checks if the encoder is turning by comparing the last value of rotaryA to the current one
        if (rotaryA.value() != rotaryB.value() and sensitivity[0] != 100): # If A and B are not equal, turning clockwise
            sensitivity[0] += 5
        elif (rotaryA.value() == rotaryB.value() and sensitivity[0] != 5): # If A and B are equal, turning counter clockwise
            sensitivity[0] -= 5
    #print(sensitivity[0]) # Prints sensitivity to the screen
    
def LED(): # Changes the state of the LED
    if (not on.value() and not off.value()): # When switch is in the center, activates sensitivity indicator
        red.duty_u16(30000-(300*sensitivity[0]))
        blue.duty_u16(300*sensitivity[0])
        green.value(0)
    elif (off.value()): # When switch is in the off position, turns LED red
        red.duty_u16(60000)
        blue.duty_u16(0)
        green.value(0)
    else: # When switch is in the on position, turns LED green
        red.duty_u16(0)
        blue.duty_u16(0)
        green.value(1)

def readhumid(): # Calculates humidity from sensor
    read = adc.read_u16() # Reads the ADC value of GPIO 26
    humidity = 100-(100*((read-water)/(air-water))) # Calculates the humidity % using the values previously defined
    if (humidity > 100): # If the percentage goes above 100%, caps it at 100%
        humidity = 100
    #print(humidity) # Prints the humidity to the terminal
    return humidity # Returns the humidity percentage

def logic(humidity): # Runs the logic for determining when to run the pump
    if (on.value()): # If manual override is pressed, run pump
        pumppower.value(1)
    elif (humidity < sensitivity[0] and not off.value()): # If off switch is off and humidity is less than sensitivity, run pump
        pumppower.value(1)
        setsensitivity() # Checks if sensitivity has changed
        time.sleep_ms(50) # Pauses script to prevent rapid cycling and crashing
    else: # Else, pump is off
        pumppower.value(0)

def main():
    setsensitivity() # Checks the rotary encoder for sensitivity updates
    LED() # Updates the state of the LED
    logic(readhumid()) # Runs the logic for the pump with the humidity percentage

while __name__ == "__main__": main()

