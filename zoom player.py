import pyautogui as pg
import time
import pyttsx3

say = pyttsx3.init()
say = pyttsx3.init()
say.setProperty("rate", 150)
say.say("Hi Enter the zoom meeting code")
say.runAndWait()
code = input("Enter the meeting code:-")

say.say("Enter You good name ")
name = input("Enter your Good Name :-")

say.say("Enter the Passcode")
pas = input("Enter the Passcode : -")


pg.hotkey("win")
pg.typewrite("zoom")
time.sleep(1)
pg.typewrite(["enter"])
time.sleep(2)
pg.moveTo(764,455)
pg.click()

time.sleep(1)
pg.typewrite(code)
time.sleep(1)
pg.moveTo(1079,543)
pg.click()
pg.hotkey("ctrl","shift","a")
time.sleep(0.2)
pg.typewrite(["backspace"])
time.sleep(1)
pg.typewrite(name)
time.sleep(0.2)
pg.moveTo(992,684)
pg.click()
time.sleep(1.5)
pg.moveTo(929,474)
time.sleep(0.5)
pg.click()
pg.typewrite(pas)
time.sleep(0.5)
pg.moveTo(975,684)
pg.click()
time.sleep(7)
pg.moveTo(964,465)
time.sleep(0.5)
pg.click()
time.sleep(2)
pg.moveTo(613,18)
time.sleep(0.7)
pg.click()
