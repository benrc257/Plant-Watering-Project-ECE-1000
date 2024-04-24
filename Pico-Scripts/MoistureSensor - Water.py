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

# Power outputs on board
pumppower = Pin(22, Pin.OUT, value=0)

# Values for humidity calculation and sensor sensitivity[0][0] (Sensor ADC outputs in air and water)
air = 30000
water = 14500
sensitivity = [80] # Humidity percentage that the pump below at

# Designates GPIO 26 as an ADC pin
adc = ADC(26)

def setsensitivity():
    lastA = rotaryA.value()
    time.sleep_ms(5)
    if (lastA != rotaryA.value()):
        if (rotaryA.value() != rotaryB.value() and sensitivity[0] != 100):
            sensitivity[0] += 5
        elif (rotaryA.value() == rotaryB.value() and sensitivity[0] != 5):
            sensitivity[0] -= 5
    print(sensitivity[0])
    
def LED():
    if (not on.value()):
        red.duty_u16(30000-(300*sensitivity[0]))
        blue.duty_u16(300*sensitivity[0])
        green.value(0)
    else:
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
    elif (humidity < sensitivity[0]): # If toggle is true and humidity is less than sensitivity, run pump
        pumppower.value(1)
        setsensitivity()
        time.sleep_ms(50)
    else: # Else, pump is off
        pumppower.value(0)

def main():
    setsensitivity() # Checks the rotary encoder for sensitivity updates
    LED() # Updates the state of the LED
    logic(readhumid()) # Runs the logic for the pump with the humidity percentage

while __name__ == "__main__": main()