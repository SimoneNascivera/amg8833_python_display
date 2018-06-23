import serial
from numpy import *
import matplotlib.pyplot as plt
from pylab import *


ser = serial.Serial('/dev/ttyUSB0')

read = 0
element = 0
counter = 0

w, h = 8, 8;
Matrix = [[0 for x in range(w)] for y in range(h)] 

x = 0;
y = 0;

while 1:
	while 1:
		char = ser.read()
	
		if read==1:
			if char==",":
				Matrix[x][y]=element
				x=x+1
				element = 0
				counter = 0
				ser.read()
			elif ord(char)==13:
				y=y+1
				x=0
				element = 0
				counter = 0
				ser.read()
			elif char == "]":
				read=0
				#print Matrix
				print "Done"
				x=0
				y=0
				break
			elif char!=".":
				element = element + int(char)*pow(10, 1-counter)
				counter = counter+1
		

		if char == "[":
			read=1


	conf_arr = np.asarray(Matrix)
	plt.matshow(conf_arr, vmin=20, vmax=50) 
	plt.colorbar()
	plt.savefig('confusion_matrix.png', format='png')
	plt.show()

