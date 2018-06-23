# amg8833_python_display
Simple python script that uses pyserial, matplotlib and numpy to graphically display the output of the AMG8833 Thermal Camera Sensor with an arduino connected to the serial port of the computer. 

## Setup
The arduino should run the "pixels_test" script from the Adafruit_AMG88xx library. 

~~~~~ python
ser = serial.Serial('/dev/ttyUSB0')
~~~~~
Insted of '/dev/ttyUSB0', insert the connected serial port
