pulse-test
==========

Simple pulse sequence for testing WS2801 LEDs with Raspberry Pi.

Instructions:
-Red LED wire to +12v
-Black LED wire to power supply and Raspberry Pi ground
-Yellow (data) LED wire to MOSI
-Green (clock) LED wire to SCLK

Command to run:
sudo python pulse.py

The script will loop forever until terminated with CTRL-C
