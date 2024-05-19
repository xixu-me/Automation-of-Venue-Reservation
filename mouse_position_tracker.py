# Copyright (c) 2024 Xi Xu, All rights reserved.

import pyautogui

print("按下 Ctrl-C 退出")
try:
    while True:
        x, y = pyautogui.position()
        positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
        print(positionStr, end="")
        print("\b" * len(positionStr), end="", flush=True)
except KeyboardInterrupt:
    print("\n")
