from pyautogui import typewrite, press
import time
time.sleep(3)
for i in range(201, 301):  # no. of times the message will be sent
    typewrite(f"Message {i} - Hey madan, I am your big fan! Say Hi, will you? plss!! :3")
    time.sleep(7)
    press("enter")
