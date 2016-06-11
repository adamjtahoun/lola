import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
import pygame
import sonar
import wheel
from threading import Thread


pygame.init()
pygame.display.set_mode([100,100])
frontDistance = -1

def getFrontDistance():
    global frontDistance
    while True:
        frontDistance = sonar.distance()
        sleep(.1) #interval of .1 seconds between reading a new distance

def update():
    for event in pygame.event.get():
	if event.type == pygame.KEYDOWN:
	    if event.key == pygame.K_w:
	        pass
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_w] and  frontDistance > 30:
        init()
        forward(0.03)
    if keystate[pygame.K_s]:
        init()
        reverse(0.03)
    if keystate[pygame.K_d]:
        init()
        rightTurn(0.03)
    if keystate[pygame.K_a]:
	    init()
	    leftTurn(0.03)
    if keystate[pygame.K_q]:
        sys.exit()
    else:
        pass
theadDistance = Thread(target= getFrontDistance(), args= ())
threadDistance.start()
while True:
    print "Distance ahead is: %d cm" %(frontDistance)
    update()
