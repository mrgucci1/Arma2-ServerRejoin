from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con




print('Press Ctrl-C to quit.');
try:
	print('waiting 5 seconds')
	time.sleep(5)
	while True:
		#First, find mulitplayer button to press
		x = pyautogui.locateOnScreen('mult.png',grayscale = True, confidence=0.6)
		if x != None:
			print('found mulitplayer button at', x)
			print('preparing to click, waiting 5 seconds')
			time.sleep(5)
			final = pyautogui.center(x)
			pyautogui.click(final)
			print('clicked')
			time.sleep(5);
			x = None;
		#find join button
		x = pyautogui.locateOnScreen('join.png',grayscale = True,confidence=0.6)
		if x != None:
			print('found join button at', x)
			print('preparing to click, waiting 5 seconds')
			time.sleep(5)
			final = pyautogui.center(x)
			pyautogui.click(final)
			print('clicked')
			time.sleep(5);
			x = None;
		#find server join button
		x = pyautogui.locateOnScreen('serverjoin.png',grayscale = True,confidence=0.6)
		if x != None:
			print('found ok button at', x)
			print('preparing to click, waiting 5 seconds')
			time.sleep(5)
			final = pyautogui.center(x)
			pyautogui.click(final)
			print('clicked')
			x = None;
		#find contuine button
		x = pyautogui.locateOnScreen('script_cont.png',grayscale = True,confidence=0.6)
		if x != None:
			print('found scrip cont button at', x)
			print('preparing to click, waiting 5 seconds')
			time.sleep(5)
			final = pyautogui.center(x)
			pyautogui.click(final)
			print('clicked')
			time.sleep(5)
			x = None;
		#click contuine on kicked message
		x = pyautogui.locateOnScreen('kicked_cont.png',grayscale = True,confidence=0.6)
		if x != None:
			print('found kicked continue at', x)
			print('preparing to click, waiting 5 seconds')
			time.sleep(5)
			final = pyautogui.center(x)
			pyautogui.click(final)
			print('clicked')
			time.sleep(5)
			x = None;
		#click refresh on kicked message
		x = pyautogui.locateOnScreen('refresh.png',grayscale = True,confidence=0.6)
		if x != None:
			print('found refresh button', x)
			print('preparing to click, waiting 5 seconds')
			time.sleep(5)
			final = pyautogui.center(x)
			pyautogui.click(final)
			print('clicked')
			time.sleep(5)
			x = None;
		#click try again when character dies
		x = pyautogui.locateOnScreen('tryagain.png',grayscale = True,confidence=0.6)
		if x != None:
			print('found try again button', x)
			print('preparing to click, waiting 5 seconds')
			time.sleep(5)
			final = pyautogui.center(x)
			pyautogui.click(final)
			print('clicked')
			time.sleep(5)
			x = None;
		#find the lets go button on character create screen
		x = pyautogui.locateOnScreen('createchar.png',grayscale = True,confidence=0.6)
		if x != None:
			print('found creatchar button', x)
			print('preparing to click, waiting 5 seconds')
			time.sleep(5)
			final = pyautogui.center(x)
			pyautogui.click(final)
			print('clicked')
			time.sleep(5)
			x = None;
		#find the random spawn button for character
		x = pyautogui.locateOnScreen('randomspawn.png',grayscale = True,confidence=0.6)
		if x != None:
			print('found randomspawn button', x)
			print('preparing to click, waiting 5 seconds')
			time.sleep(5)
			final = pyautogui.center(x)
			pyautogui.click(final)
			print('clicked')
			time.sleep(5)
			x = None;
		print("sleeping for 2 minutes")
		time.sleep(120)
except KeyboardInterrupt:
	print('\nDone')
	