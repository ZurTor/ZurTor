#!/usr/bin/python
import pyautogui
import time

message = input("What message do you want to keep sending? (Leave this blank if you want to paste your clipboard)  ")
repeats = int(input("How many times do you want to send the message?  "))
delay = int(input("How many milliseconds do you want to wait in between each message?  "))

isLoaded = input("Press Enter when your messaging app is loaded up.")



print("You have five seconds to refocus the text input area of your messaging app")

time.sleep(5)


for i in range(0,repeats):         #Message sending loop
	if message != "":
		pyautogui.typewrite(str(i))
		pyautogui.press("enter")
	else:
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.press("enter")

	time.sleep(delay/1000)


print("Done\n")
