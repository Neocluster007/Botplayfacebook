import init

def Generate_Image_FoodThai(title):
    """
    เรียก Gemini API เพื่อสร้างเนื้อเรื่อง
    """

    user_story_prompt = """
        A photorealistic, top-down shot of """+title+""", beautifully plated on a modern ceramic dish. The lighting is soft and natural, highlighting the textures and vibrant colors of the ingredients. There are subtle garnishes like fresh herbs or a sprinkle of spice. The background is a clean, minimalist wooden table, slightly out of focus to emphasize the dish.
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
                    with open(init.file_ThaiFood, 'wb') as f:
                        # เขียนข้อมูล (content) ของ response ซึ่งเป็น bytes ของรูปภาพ
                        f.write(response.content)
                    print(f"ดาวน์โหลดรูปภาพสำเร็จ บันทึกเป็น: {init.file_ThaiFood}")

                    return init.file_ThaiFood
                else:
                    print(f"ดาวน์โหลดไม่สำเร็จ Status code: {response.status_code}")

                    Generate_Image_FoodThai(title)

            except init.requests.exceptions.RequestException as e:
                print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")

            return image_url
        else:
            print("ไม่ได้รับการตอบกลับจาก Gemini")
            return None
            
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการเรียก Gemini API: {e}")
        return None

def Genarate_Content_ThaiFood():
    import random
    menu_100 = [
        "กุ้งแม่น้ำเผา (มันกุ้งเยิ้มๆ)",
        "ปูไข่นึ่งนมสด",
        "ปลากะพงทอดน้ำปลา",
        "ส้มตำปูปลาร้า (ใส่พริกเยอะๆ)",
        "หมูกรอบ (หนังฟูๆ)",
        "คอหมูย่าง (ติดมันฉ่ำๆ)",
        "ซี่โครงหมูบาร์บีคิว (ซอสชุ่มๆ)",
        "สเต็กเนื้อโทมาฮอว์ก (ย่างแบบมีเดียมแรร์)",
        "แซลมอนซาซิมิ (ลายสวยๆ)",
        "ข้าวหน้าปลาไหล (อูนางิ)",
        "ต้มยำกุ้งน้ำข้น",
        "หมูกระทะ (ย่างเนย)",
        "ชาบูน้ำดำ (เนื้อสไลด์ลวก)",
        "ชีสเบอร์เกอร์ (ดับเบิ้ลชีส)",
        "พิซซ่า (หน้าเปปเปอโรนี ชีสยืดๆ)",
        "ผัดไทยกุ้งสด (ห่อไข่)",
        "ข้าวซอยไก่ (น่องไก่เปื่อยๆ)",
        "ข้าวขาหมู (เนื้อ หนัง คากิ)",
        "ข้าวมันไก่ (ตบ)",
        "ข้าวหมูแดง หมูกรอบ (ราดน้ำฉ่ำๆ)",
        "ลาบหมู (คั่วสุก)",
        "น้ำตกเนื้อ",
        "ไก่ทอดเกาหลี (ซอสการ์ลิค/ซอสเผ็ด)",
        "ทงคัตสึ (สันนอก)",
        "ราเมงทงคตสึ (ใส่ไข่ดอง)",
        "ปูผัดผงกะหรี่",
        "กุ้งแช่น้ำปลา",
        "ยำปูม้า",
        "หอยนางรมสด (ทรงเครื่อง)",
        "เล้งแซ่บ (พริกเต็มชาม)",
        "แกงเขียวหวานไก่ (ใส่ยอดมะพร้าว)",
        "ไข่เจียวปู (ฟูๆ)",
        "ต้มข่าไก่",
        "มัสมั่นไก่ (น่องติดสะโพก)",
        "ผัดกะเพราหมูสับ (คลุกข้าว ไข่ดาวไม่สุก)",
        "หมูสามชั้นทอดน้ำปลา",
        "ไก่ย่าง (หนังกรอบ)",
        "เสือร้องไห้ (จิ้มแจ่ว)",
        "ก๋วยเตี๋ยวเรือน้ำตก (เข้มข้น)",
        "ก๋วยเตี๋ยวต้มยำ (น้ำขลุกขลิก)",
        "ติ่มซำ (ฮะเก๋า, ขนมจีบกุ้ง)",
        "เสี่ยวหลงเปา (น้ำซุปข้างใน)",
        "หมูหัน (หนังกรอบ)",
        "เป็ดปักกิ่ง",
        "หม่าล่า (ปิ้งย่าง/หม้อไฟ)",
        "ยำแซลมอน",
        "กุ้งถัง (ซอสเนยกระเทียม)",
        "หอยทอด (แป้งกรอบ)",
        "ออส่วน (หอยนางรมตัวใหญ่ๆ)",
        "ผักโขมอบชีส",
        "ลาซานญ่าเนื้อ",
        "สปาเก็ตตี้คาโบนาร่า (ครีมมี่)",
        "สปาเก็ตตี้ขี้เมาทะเล",
        "บิบิมบับ (ข้าวยำเกาหลี)",
        "ต็อกบกกี (ใส่ชีส)",
        "หมูย่างเกาหลี (ซัมกยอบซัล)",
        "คั่วกลิ้งหมูสับ",
        "สะตอผัดกะปิกุ้ง",
        "ใบเหลียงผัดไข่",
        "แกงส้มชะอมกุ้ง",
        "ขนมจีนน้ำยาปู",
        "ไส้กรอกอีสาน (ย่างเตาถ่าน)",
        "ซุปหน่อไม้",
        "ตำข้าวโพดไข่เค็ม",
        "ตำหลวงพระบาง (เส้นมะละกอแผ่น)",
        "หมูสะเต๊ะ (จิ้มน้ำจิ้มถั่ว)",
        "ทาโกะยากิ (ไส้ปลาหมึก)",
        "เทมปุระกุ้ง",
        "ซูชิฟัวกราส์ (ตับห่าน)",
        "ซูชิโอโทโร่ (ส่วนท้องปลาทูน่า)",
        "ไข่ดองซีอิ๊ว (กินกับข้าวญี่ปุ่นร้อนๆ)",
        "แจ่วฮ้อน",
        "จิ้มจุ่ม",
        "ฉู่ฉี่ปลาเนื้ออ่อน",
        "ยำไข่แมงดา",
        "ปูนิ่มทอดกระเทียม",
        "หมึกผัดไข่เค็ม",
        "หมึกย่าง (น้ำจิ้มซีฟู้ดแซ่บๆ)",
        "เฟรนช์ฟรายส์ (ราดชีส)",
        "ชีสบอล (ยืดๆ)",
        "ไก่ทอดหาดใหญ่ (หอมเจียวเยอะๆ)",
        "ข้าวเหนียวมะม่วง",
        "บิงซู (มะม่วง/สตอเบอรี่)",
        "ฮันนี่โทสต์ (ไอศกรีมวานิลลา)",
        "ช็อกโกแลตลาวา (เยิ้มๆ)",
        "บราวนี่ (อุ่นๆ)",
        "เครปเย็น (ไส้ทะลัก)",
        "โรตี (กล้วย+ไข่+นมข้น)",
        "บลูเบอร์รี่ชีสเค้ก",
        "ปาท่องโก๋ (จิ้มสังขยา/นมข้น)",
        "ขนมปังปิ้ง (เนย นม น้ำตาล)",
        "ชานมไข่มุก (บราวน์ชูการ์)",
        "ครัวซองต์ (อบใหม่ๆ)",
        "แพนเค้ก (ราดเมเปิ้ลไซรัป)",
        "เอแคลร์ (ไส้ครีม)",
        "ทุเรียน (หมอนทอง)",
        "แมคแอนด์ชีส (Mac and Cheese)",
        "กุ้งอบวุ้นเส้น",
        "หอยแครงลวก (จิ้มซีฟู้ด)",
        "ข้าวผัดปู"
    ]

    random_menu = random.choice(menu_100)
    print(f"เมนูที่สุ่มได้คือ: {random_menu}")
    locationfile = Generate_Image_FoodThai(random_menu)

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
            "title":random_menu,
            "locationfile":new_path
        }   
    ]
    return ret
    


