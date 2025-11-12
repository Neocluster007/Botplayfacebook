import schedule
import time
import datetime

# --- Import โมดูลของคุณ ---
import genThaifood
import genSunset
import PostFacebook

# --- ตั้งค่าเวลา ---
# เวลาที่สามารถทำงานได้ (Active Time)
# (อนุญาตให้ทำงานตั้งแต่ 05:30:00 จนถึง 23:29:59)
ACTIVE_START = datetime.time(5, 30, 0)
ACTIVE_END = datetime.time(23, 30, 0) # หยุดทำงานตอน 23:30

# เวลาที่ต้องการให้รัน Sunset
MORNING_RUN = "07:00"
EVENING_RUN = "18:00"

# --- ฟังก์ชันเช็กเวลา (ห้ามทำงานตอนกลางคืน) ---
def is_active_time():
    """
    เช็กว่าตอนนี้อยู่ในเวลาที่อนุญาตให้ทำงานหรือไม่
    (อนุญาต: 05:30 - 23:29:59)
    """
    now = datetime.datetime.now().time()
    
    # เงื่อนไขคือ: ต้องอยู่ในช่วงเวลา ACTIVE_START และ ACTIVE_END
    # ถ้าเวลาข้ามคืน (เช่น 23:30 - 05:30) ตรรกะจะซับซ้อน
    # แต่นี่คือ 05:30 - 23:30 (อยู่ในวันเดียวกัน)
    
    if ACTIVE_START <= now < ACTIVE_END:
        return True
    else:
        return False

# --- ฟังก์ชันสำหรับงาน (Jobs) ---

def job_thaifood():
    """
    งานที่ต้องทำทุก 15 นาที: สร้างเนื้อหา ThaiFood และโพสต์
    """
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Running ThaiFood Job...")
    try:
        ThaiFood = genThaifood.Genarate_Content_ThaiFood()
        
        if ThaiFood and len(ThaiFood) > 0:
            print(f"  > Generated: {ThaiFood[0]['title']}")
            # PostFacebook.postFacebook(ThaiFood[0])
            print("  > (Simulated) Facebook Post Complete.")
        else:
            print("  > genThaifood did not return valid content.")

        PostFacebook.postFacebook(ThaiFood[0]['title'],ThaiFood[0]['locationfile'])
            
    except Exception as e:
        print(f"  > ERROR during job_thaifood: {e}")

def job_sunset():
    """
    งานที่ต้องทำวันละ 2 ครั้ง: สร้างเนื้อหา Sunset
    """
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Running Sunset Job...")
    try:
        Sunset = genSunset.Genarate_Content_Sunset()
        print(f"  > Generated Sunset: {Sunset}")
        # ถ้าต้องการโพสต์ Sunset ด้วย ก็เรียก PostFacebook ที่นี่
        # PostFacebook.postFacebook(Sunset[0]) 
        PostFacebook.postFacebook(Sunset[0]['title'],Sunset[0]['locationfile'])
        
    except Exception as e:
        print(f"  > ERROR during job_sunset: {e}")


# --- ตั้งค่าตารางเวลา (Scheduling) ---
print("Starting scheduler...")
print(f"Quiet time is from {ACTIVE_END} to {ACTIVE_START}")

# 1. ตั้งเวลา ThaiFood
schedule.every(15).to(20).minutes.do(job_thaifood)

# 2. ตั้งเวลา Sunset
schedule.every().day.at(MORNING_RUN).do(job_sunset)
schedule.every().day.at(EVENING_RUN).do(job_sunset)

# --- ลูปการทำงานหลัก (Main Loop) ---
print("Scheduler is running. Press Ctrl+C to stop.")

#job_thaifood()

#PostFacebook.postFacebook("terst","E:\BOT\Botplayfacebook\source\ThaiFood.jpg")

# รันครั้งแรกทันที (ถ้าอยู่ในเวลาทำงาน)
# เพื่อไม่ต้องรอ 15 นาทีแรก
if is_active_time():
    print("Running initial jobs on startup...")
    job_thaifood()
    # ไม่รัน job_sunset ทันที เพราะมันต้องรันตามเวลา
else:
    print("Startup is during quiet time. Waiting for active time...")

while True:
    try:
        if is_active_time():
            # ถ้าอยู่ในเวลาทำงาน: ให้ schedule ตรวจสอบว่ามีงานค้างไหม
            schedule.run_pending()
            time.sleep(1) # ตรวจสอบทุก 1 วินาที
        else:
            # ถ้าอยู่นอกเวลาทำงาน (23:30 - 05:30):
            now_str = datetime.datetime.now().strftime('%H:%M:%S')
            print(f"[{now_str}] Quiet time. Sleeping for 10 minutes...")
            # ไม่ต้องเช็กบ่อย ให้พักไปเลย 10 นาที
            time.sleep(600) 
            
    except KeyboardInterrupt:
        print("\nScheduler stopped by user.")
        break
    except Exception as e:
        print(f"An unexpected error occurred in the main loop: {e}")
        time.sleep(60) # พัก 1 นาทีก่อนลองใหม่