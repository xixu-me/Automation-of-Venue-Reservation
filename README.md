# 场地预订自动化

本存储库提供了填写[表单《纺大阳光校区羽毛球馆场地预订》](https://www.chaojibiaodan.com/form/1d1u2Nk8)的自动化脚本。

## 运行环境

- Windows 操作系统
- Microsoft Edge 浏览器
- Python 3.6 或更高版本
- PyAutoGUI 库
- Pyperclip 库

你可以使用以下命令来安装所需的库：

```bash
pip install pyautogui
pip install pyperclip
```

## 使用方法

1. 下载脚本文件 [`reservation.py`](https://github.com/xixu-zg/Automation-of-Venue-Reservation/blob/main/reservation.py)；
2. 填写脚本中的表单信息；
3. 脚本中的坐标可能需要根据你的屏幕分辨率进行调整，你可以使用 [`mouse_position_tracker.py`](https://github.com/xixu-zg/Automation-of-Venue-Reservation/blob/main/mouse_position_tracker.py) 来通过追踪鼠标位置来获取坐标；
4. 将 Microsoft Edge 浏览器拖拽至屏幕右边缘，使其占据屏幕右半部分；
5. 运行脚本即可，脚本会自动填写表单并提交。

## 效果展示



## 注意事项

- 本存储库仅供学习交流使用，不得用于任何商业用途。
- 请勿滥用脚本，以免对他人造成困扰。
- 请勿将脚本用于非法用途，否则后果自负。
