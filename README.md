# Automatic Plant Watering

This project was completed for Dr. Bhattacharya's ECE 1000 class. The goal was to create an automatic plant watering system using a soil moisture sensor.

## Description

Using a Capacitive Soil Moisture Sensor (HW-390), a Single-Channel Relay (Keyes-SR1y), a rotary encoder (KY-040), a switch, a small pump, an RGB LED, a Raspberry Pi Pico WH, and an accompanying breakout board, I designed a device for detecting the water level or humidity of a hydroponic/geoponic system. A pump wired into a relay is powered when the water level is detected to be low by the soil moisture sensor and will pump water from a reservoir into the container. A rotary encoder is included to enable easy adjustment of the desired moisture level, and the LED serves as a visual indicator. The switch can be used to manually activate the pump. 

### Dependencies

* [MicroPython](https://micropython.org/)

### Installing/Executing

* Step 1 - Download [Thonny IDE](https://thonny.org/) and install
* Step 2 - Launch Thonny and select the Run dropdown
* Step 3 - Select "Configure interpreter" and choose "MicroPython (Raspberry Pi Pico)" from the dropdown menu
* Step 4 - Connect the Rasberry Pi Pico to the computer via USB
* Step 5 - Open the script and run it using Thonny
  * The required pins for the sensor, relay, encoder, switch, and pump are defined in the script

## Authors

Benjamin Clark (brclark44@tntech.edu)

## Sources

* [Raspberry Pi Pico WH Documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
* [MicroPython Documentation](https://docs.micropython.org/en/latest/)
* [Guide to rotary encoder](https://howtomechatronics.com/tutorials/arduino/rotary-encoder-works-use-arduino/)
* [Guide to moisture sensor](https://how2electronics.com/interface-capacitive-soil-moisture-sensor-arduino/)
