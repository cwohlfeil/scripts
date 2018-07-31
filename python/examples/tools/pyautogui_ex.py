import pyautogui

# Failsafes in case goes haywire
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# Get screen size
pyautogui.size()
width, height = pyautogui.size()

i = 1
while i < 10:
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)
        i += 1

pyautogui.position()
