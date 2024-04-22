# Automatic Plant Watering

This project was completed for Dr.Bhattacharya's ECE 1000 class. The goal was to create an automatic plant watering system using a soil moisture sensor.

## Description

Using a Capacitive Soil Moisture Sensor (HW-390), a Single-Channel Relay (Keyes-SR1y), a small pump, a Raspberry Pi Pico WH, and an accompanying breakout board, I designed a device for detecting the water level or humidity of a hydroponic/geoponic system. The script is configured to work best in a hydroponic system. A pump wired into a relay is powered when the water level is detected to be low by the soil moisture sensor and will pump water from a reservoir into the container until the water reaches halfway up the sensor. On the breakout board, there are three buttons: a manual override to activate the pump, and two manual overrides to stop the pump (held and toggled).

### Dependencies

* [MicroPython](https://micropython.org/)

### Installing/Executing

* Step 1 - Download [Thonny IDE](https://thonny.org/) and install
* Step 2 - Launch Thonny and select the Run dropdown
* Step 3 - Select "Configure interpreter" and choose "MicroPython (Raspberry Pi Pico)" from the dropdown menu
* Step 4 - Connect the Rasberry Pi Pico in bootsel mode (method varies by board)
* Step 5 - Open the script and run it using Thonny
  * The required pins for the sensor, relay, buttons, and pump are defined in the script

## Authors

Benjamin Clark (brclark44@tntech.edu, +1(281)638-6006)

## Sources

* [Raspberry Pi Pico WH Documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
* [MicroPython Documentation](https://docs.micropython.org/en/latest/)
