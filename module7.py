##############################################
# File Name: module7.py
# Version: 1.0
# Team No.: 21
# Team Name:
# Date: 11 Nov 15
##############################################

import RPi.GPIO as GPIO
import time

print 'Programming the PiBot...'

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def forward(interval):
      print 'forward'
      GPIO.output(11, True)
      GPIO.output(13, True)
      time.sleep(interval)
      GPIO.output(11, False)
      GPIO.output(13, False)
   
def back(interval):
      print 'back'
      GPIO.output(7, True)
      GPIO.output(15, True)
      time.sleep(interval)
      GPIO.output(7, False)
      GPIO.output(15, False)

def left(interval):
      print 'right'
      GPIO.output(13, True)
      time.sleep(interval)
      GPIO.output(13, False)
      
def right(interval):
      print 'left :)'
      GPIO.output(11, True)
      time.sleep(interval)
      GPIO.output(11, False)

# Main instructions here      
forward(2)
right(4)
left(2)
back(2)
print 'breakdance!!!'
right(0.4)
left(0.4)
right(0.4)
left(0.4)
back(0.5)
forward(0.5)
back(0.5)
forward(0.5)
back(0.5)
forward(0.5)
right(0.4)
left(0.4)
right(0.4)
left(0.4)
back(0.5)
forward(0.5)
back(0.5)
forward(0.5)
back(0.5)
forward(0.5)
print 'DONUTZZ!!!!'
right(4)
left(4)


GPIO.cleanup()
   
print "\nPiBot is going offline..."
