# Copyright (c) 2024 Xi Xu, All rights reserved.

############## 请在此处填写表单信息 ##############
学号 = "0000000000"
姓名 = "你的姓名"
学院 = "你的学院"
手机号码 = "12345678901"
预订日期 = "2024-09-01"  # 格式为 "YYYY-MM-DD"
预订时段 = False  # True: 周一至周五时段，False: 周六、周日时段
周一至周五时段 = 0  # 0: 08:00--09:30, 1: 11:30--13:30, 2: 17:30--19:30, 3: 19:30--21:30
周六周日时段 = 0  # 0: 09:30--11:30, 1: 11:30--13:30, 2: 13:30--15:30, 3: 15:30--17:30, 4: 17:30--19:30, 5: 19:30--21:30
##################################################

import numpy as np
import pyautogui as pag
import pyperclip as ppc
import time
from PIL import Image

pag.click(x=1200, y=75)
pag.typewrite("https://www.chaojibiaodan.com/form/1d1u2Nk8")
pag.press("enter")
while Image.fromarray(np.array(pag.screenshot(region=(1165, 35, 1, 1)))).getpixel(
    (0, 0)
) != (49, 193, 123):
    time.sleep(0.5)
pag.click(x=1020, y=275)
pag.typewrite(学号)
pag.click(x=1020, y=380)
ppc.copy(姓名)
pag.hotkey("ctrl", "v")
pag.click(x=1020, y=485)
ppc.copy(学院)
pag.hotkey("ctrl", "v")
pag.click(x=1020, y=590)
pag.typewrite(手机号码)
pag.click(x=1020, y=735)
pag.typewrite(预订日期)
if 预订时段:
    pag.click(x=1020, y=880)
    pag.scroll(-1000)
    pag.click(x=1020, y=385)
    pag.click(x=1020, y=445 + 25 * 周一至周五时段)
else:
    pag.click(x=1020, y=930)
    pag.scroll(-1000)
    pag.click(x=1020, y=525)
    pag.click(x=1020, y=590 + 25 * 周六周日时段)
pag.click(x=1020, y=730)
pag.click(x=1440, y=820)
