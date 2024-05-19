import pyautogui as pag
import pyperclip as ppc
import time

############## 请在此处填写信息 ##############
学号 = "2021000000"
姓名 = "张三"
学院 = "计算机与人工智能学院"
手机号码 = "12345678901"
预订日期 = "2024-09-01"
预订时段 = True  # True: 周一至周五时段，False: 周六、周日时段
周一至周五时段 = 0  # 0: 08:00--09:30, 1: 11:30--13:30, 2: 17:30--19:30, 3: 19:30--21:30
周六周日时段 = 0  # 0: 09:30--11:30, 1: 11:30--13:30, 2: 13:30--15:30, 3: 15:30--17:30, 4: 17:30--19:30, 5: 19:30--21:30
##############################################
网页加载时间 = 3  # 根据网速调整
##############################################

pag.click(x=1200, y=75)
pag.typewrite("https://www.chaojibiaodan.com/form/1d1u2Nk8")
pag.press("enter")
time.sleep(网页加载时间)
pag.click(x=1015, y=275)
pag.typewrite(学号)
pag.click(x=1015, y=380)
ppc.copy(姓名)
pag.hotkey("ctrl", "v")
pag.click(x=1015, y=485)
ppc.copy(学院)
pag.hotkey("ctrl", "v")
pag.click(x=1015, y=590)
pag.typewrite(手机号码)
pag.click(x=1015, y=735)
pag.typewrite(预订日期)
if 预订时段:
    pag.click(x=1015, y=880)
    pag.scroll(-1000)
    pag.click(x=1015, y=365)
    pag.click(x=1015, y=425 + 25 * 周一至周五时段)
else:
    pag.click(x=1015, y=930)
    pag.scroll(-1000)
    pag.click(x=1015, y=505)
    pag.click(x=1015, y=570 + 25 * 周六周日时段)
pag.click(x=1015, y=715)
pag.click(x=1430, y=800)