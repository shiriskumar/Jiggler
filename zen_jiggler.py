import pyautogui,  sys
from time import sleep

pyautogui.FAILSAFE= False
print("Keys on Job!\n\nHit Ctrl+C to stop.")
while True:
	try:
		pyautogui.press('up')
		pyautogui.press('down')
		sleep(3)
	except (KeyboardInterrupt, SystemExit):
		print("Buhbye!")
		sys.exit()