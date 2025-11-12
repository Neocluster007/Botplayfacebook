import pyautogui
while True:
    # อ่านค่าตำแหน่งเมาส์ (X, Y)
    x, y = pyautogui.position()

    print(f"ตำแหน่งเมาส์ปัจจุบัน: X = {x}, Y = {y}")