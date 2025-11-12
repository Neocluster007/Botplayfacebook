import init

def postFacebook(title,location_file):
    
    try:
        program_files = init.os.environ.get("ProgramFiles", "C:\\Program Files")
        CHROME_PATH = init.os.path.join(program_files, "Google\\Chrome\\Application\\chrome.exe")
        if not init.os.path.exists(CHROME_PATH):
            program_files_x86 = init.os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)")
            CHROME_PATH = init.os.path.join(program_files_x86, "Google\\Chrome\\Application\\chrome.exe")
        
        local_app_data = init.os.environ.get("LOCALAPPDATA", "C:\\Users\\YOUR_USERNAME\\AppData\\Local")
        PROFILE_PATH_BASE = init.os.path.join(local_app_data, "Google\\Chrome\\User Data")

    except Exception:
        print("หา Path อัตโนมัติไม่เจอ, กรุณาใส่ Path ด้วยตัวเอง")
        CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        PROFILE_PATH_BASE = "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Google\\Chrome\\User Data"

    PROFILE_DIRECTORY = "Default"
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 800
    URL_TO_OPEN = f"https://www.facebook.com/neocluster08/"

    print(f"กำลังเปิด Google Chrome จาก: {CHROME_PATH}")
    command = [
        CHROME_PATH,
        f"--user-data-dir={PROFILE_PATH_BASE}",
        f"--profile-directory={PROFILE_DIRECTORY}",
        f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}",
        URL_TO_OPEN
    ]
    try:
        #init.subprocess.Popen(command)
        print("\nChrome ถูกเปิดแล้ว (กระบวนการทำงานในพื้นหลัง)")
    except Exception as e:
        print(f"!!! ข้อผิดพลาดในการเปิด Chrome: {e}")
        exit()

    print("กำลังเริ่มติดตามตำแหน่งเมาส์...")
    print("กด Ctrl+C ในหน้าต่างนี้ เพื่อหยุดการติดตาม")
    mouse = init.MouseController()
    init.pyautogui.click(1200, 600)
    init.time.sleep(1.5)
    init.pyautogui.press('F5')
    init.time.sleep(1.5)
    init.pyautogui.click(729, 191)
    init.time.sleep(5.5)
    init.pyautogui.click(844, 765)
    init.time.sleep(2.5)
    init.pyautogui.click(377, 745)
    init.time.sleep(2.5)
    init.pyperclip.copy(location_file)
    init.time.sleep(0.5)
    init.pyautogui.hotkey('ctrl', 'v')
    init.time.sleep(0.5)
    init.pyautogui.press('enter')
    init.time.sleep(1.5)
    init.pyautogui.click(571, 442)
    init.time.sleep(1.5)
    init.pyperclip.copy(title)
    init.time.sleep(0.5)
    init.pyautogui.hotkey('ctrl', 'v')
    init.time.sleep(1.5)
    init.pyautogui.click(639, 766)
    init.time.sleep(2.5)
    init.pyautogui.click(639, 756)
    init.time.sleep(1.5)