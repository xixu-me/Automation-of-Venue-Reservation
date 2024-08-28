# Copyright (c) 2024 Xi Xu, all rights reserved.

############## 请在此处填写表单信息 ##############
学号 = "2000000000"
姓名 = "你的姓名"
学院 = "你的学院"
手机号码 = "12345678901"
预订日期 = "2024-09-01"  # 格式为 "YYYY-MM-DD"
预订时段 = False  # True: 周一至周五时段，False: 周六、周日时段
周一至周五时段 = 0  # 0: 08:00--09:30, 1: 11:30--13:30, 2: 17:30--19:30, 3: 19:30--21:30
周六周日时段 = 0  # 0: 09:30--11:30, 1: 11:30--13:30, 2: 13:30--15:30, 3: 15:30--17:30, 4: 17:30--19:30, 5: 19:30--21:30
##################################################

import pyautogui as pag
from PIL import Image
import numpy as np
import time
import pyperclip as ppc

pag.click(x=1200, y=75)  # 地址栏坐标
pag.typewrite("https://www.chaojibiaodan.com/form/1d1u2Nk8")
pag.press("enter")
favicon_pos = (1165, 35)  # 网页图标坐标
while Image.fromarray(
    np.array(pag.screenshot(region=(favicon_pos[0], favicon_pos[1], 1, 1)))
).getpixel((0, 0)) != (49, 193, 123):
    time.sleep(0.1)
pag.click(x=1020, y=275)  # “学（工）号”输入框坐标
pag.typewrite(学号)
pag.click(x=1020, y=380)  # “姓名”输入框坐标
ppc.copy(姓名)
pag.hotkey("ctrl", "v")
pag.click(x=1020, y=485)  # “学院”输入框坐标
ppc.copy(学院)
pag.hotkey("ctrl", "v")
pag.click(x=1020, y=590)  # “手机号码”输入框坐标
pag.typewrite(手机号码)
pag.click(x=1020, y=735)  # “预订日期”输入框坐标
pag.typewrite(预订日期)
if 预订时段:
    pag.click(x=1020, y=880)  # “周一--周五时段”单选框坐标
    pag.scroll(-1000)
    pag.click(x=1020, y=385)  # “周一至周五时段”菜单下拉按钮坐标
    pag.click(x=1020, y=445 + 25 * 周一至周五时段)  # “周一至周五时段”菜单选项坐标
else:
    pag.click(x=1020, y=930)  # “周六、周日时段”单选框坐标
    pag.scroll(-1000)
    pag.click(x=1020, y=525)  # “周六、周日时段”菜单下拉按钮坐标
    pag.click(x=1020, y=590 + 25 * 周六周日时段)  # “周六、周日时段”菜单选项坐标
pag.click(x=1020, y=730)  # “我已知晓查询方式”单选框坐标
pag.click(x=1440, y=820)  # 提交按钮坐标
