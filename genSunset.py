import init

def Generate_Image_Sunset(title):
    """
    เรียก Gemini API เพื่อสร้างเนื้อเรื่อง
    """


    user_story_prompt = """
        A photorealistic first-person perspective from the ground level of serene Thai rice fields at """+title+""". The viewer is standing among the lush green rice paddies, with water gently reflecting the soft golden light. The vast expanse of the fields stretches into the distance, with the warm colors of the sky – oranges, pinks, and purples – dominating the horizon. A few traditional Thai elements like distant houses or palm trees might be subtly visible. The foreground features detailed rice stalks, creating an immersive and peaceful atmosphere
    """
    
    #print("กำลังติดต่อ Gemini เพื่อสร้างรูป")
    try:
        # (ใช้ gemini-pro ที่เสถียรและใช้งานได้)
        model = init.genaiA.GenerativeModel(
            model_name="gemini-2.5-flash"
        )
        response = model.generate_content(user_story_prompt)
        
        if response and response.text:

            import random
            from urllib.parse import quote

            # --- ตั้งค่าตัวแปร ---
            width = 1920
            height = 1080
            random_seed = random.randint(0, 99999) # เทียบเท่า Math.floor(Math.random() * 100000)

            # (สำคัญ!) ส่วนนี้ ($input.first().json.output) เป็นโค้ดเฉพาะแพลตฟอร์ม
            # ใน Python คุณต้องกำหนดค่า `final_prompt` นี้เอง
            # 
            # ตัวอย่าง:
            final_prompt = response.text.encode("utf-8")
            # -----------------------------------------------------------------


            # สร้าง URL โดยมีการเข้ารหัส (encode) prompt
            image_url = f"https://image.pollinations.ai/prompt/{quote(final_prompt)}.jpg?width={width}&height={height}&seed={random_seed}&model=flux&nologo=true"

            # สร้างผลลัพธ์ (ใน Python คือ list ที่มี dictionary อยู่ข้างใน)
            result = [
                {
                    "json": {
                        "text": final_prompt,
                        "imageUrl": image_url
                    }
                }
            ]

            # พิมพ์ผลลัพธ์ (หรือ return ถ้าคุณใช้ในฟังก์ชัน)
            #print(image_url)

            import time
            time.sleep(30)

            try:
                # ส่ง HTTP GET request ไปที่ URL
                response = init.requests.get(image_url)

                # ตรวจสอบว่า request สำเร็จหรือไม่ (status code 200 คือสำเร็จ)
                if response.status_code == 200:
                    # เปิดไฟล์ในโหมด 'write binary' ('wb')
                    with open(init.file_Sunset, 'wb') as f:
                        # เขียนข้อมูล (content) ของ response ซึ่งเป็น bytes ของรูปภาพ
                        f.write(response.content)
                    print(f"ดาวน์โหลดรูปภาพสำเร็จ บันทึกเป็น: {init.file_Sunset}")

                    return init.file_Sunset
                else:
                    print(f"ดาวน์โหลดไม่สำเร็จ Status code: {response.status_code}")

                    Generate_Image_Sunset(title)

            except init.requests.exceptions.RequestException as e:
                print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")

            return image_url
        else:
            print("ไม่ได้รับการตอบกลับจาก Gemini")
            return None
            
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการเรียก Gemini API: {e}")
        return None

def Genarate_Content_Sunset():

    import datetime

    # 1. ดึงเวลาปัจจุบัน
    now = datetime.datetime.now()
    current_hour = now.hour

    timestr = ""

    # 2. ตรวจสอบช่วงเวลา (ปรับเกณฑ์ได้ตามต้องการ)
    if 5 <= current_hour < 12:  # 5:00 - 11:59
        period = "sunrise"
        timestr = "เช้าแล้วอย่าลืมไปมีปฏิสัมพันธ์เยี่ยมบ้านเพื่อนนะครับ ♥️♥️♥️"
        
    elif 17 <= current_hour <= 23: # 17:00 - 20:59
        period = "sunset"
        timestr = "ค่ำแล้วอย่าลืมไปมีปฏิสัมพันธ์เยี่ยมบ้านเพื่อนนะครับ ♥️♥️♥️"
    else:
        period = "ช่วงเวลาอื่น" # สำหรับเวลาที่ไม่ใช่เช้าหรือเย็น (เช่น บ่าย หรือ กลางคืน)
        return None


    # 3. แสดงผล
    print(f"เวลาปัจจุบัน: {now.strftime('%H:%M')}")
    print(f"ตอนนี้เป็น {period}")

    locationfile = Generate_Image_Sunset(period)

    import os
    import os.path

    # 1. ดูว่าตอนนี้อยู่ที่โฟลเดอร์ไหน (Get Current Working Directory)
    current_path = os.getcwd()
    new_path = current_path.replace("\\", "/")
    new_path = new_path+"/"+locationfile
    new_path = new_path.replace("/","\\")
    print(f"ตอนนี้อยู่ที่: {new_path}")

    ret =[
        {
            "title":timestr,
            "locationfile":new_path
        }   
    ]
    return ret
    

