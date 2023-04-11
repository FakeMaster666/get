#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import RPi.GPIO as gpio
import sys
dac=[26, 19, 13, 6, 5, 11, 9, 10]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
def perev(a, n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]
try:
    while (True):
        a=input('input 0-255')
        if a=='q':
            sys.exit()
        elif  a.isdigit() and int(a)%1==0 and 0<=int(a)<=255:
            gpio.output(dac, perev(int(a), 8))
            print("{:.4f}".format(int(a)/256*3.3))
        elif not a.isdigit():
            print('input number 0-255sdfgsfd')
    
        
except ValueError:
    print('input number 0-255')
except KeyboardInterrupt:
    print('done')
finally:
    gpio.output(dac, 0)
    gpio.cleanup()


# In[ ]:


import RPi.GPIO as gpio
import sys
from time import sleep
dac=[26, 19, 13, 6, 5, 11, 9, 10]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
def perev(a, n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]

try:
    while (True):
        T=input()
        if not T.isdigit():
            print('vvedi pozalusrta chislo')
        t=T/256/2
        for i in range(256):
            gpio.output(dac, perev(i, 8))
            sleep(t)
        for i in range(255, -1, -1):
            gpio.output(dac, perev(i, 8))
            sleep(t)
finally:
    gpio.output(dac, 1)
    gpio.cleanup()
  

