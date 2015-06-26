import RPi.GPIO as GPIO
import time
import pygame.mixer
from time import sleep
import random

file1 = "/home/pi/bean.wav"
file2 = "/home/pi/bean1.wav"
file3 = "/home/pi/bean2.wav"

pygame.mixer.init(48000, -16, 1, 1024)

channelA = pygame.mixer.Channel(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

filenum = 0
count = 0
isReleased = True

while True:
	inputValue = GPIO.input(23)
	if(inputValue == True and isReleased == True):
		filenum = random.randrange(1, 4)
				
		if(filenum == 1):
			sound = pygame.mixer.Sound(file1)
		if(filenum == 2):
			sound = pygame.mixer.Sound(file2)
		if(filenum == 3):
			sound = pygame.mixer.Sound(file3)
		channelA.play(sound)

		sleep(2.0)
		isReleased = False
	if(inputValue == False and isReleased == False):	
		isReleased = True
	time.sleep(.01)

