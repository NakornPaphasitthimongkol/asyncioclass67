import asyncio
import random

async def cook_rice():
    cook_time = 1 + random.random()  # กำหนดเวลาทำอาหารแบบสุ่มระหว่าง 1 ถึง 2 วินาที
    print(f"Microwave (Rice): Cooking {cook_time} seconds...")  # แสดงข้อความบอกเวลาทำอาหาร
    await asyncio.sleep(cook_time)  # หยุดการทำงานตามเวลาที่กำหนดเพื่อจำลองการทำอาหาร
    print("Microwave (Rice): Finished cooking")  # แสดงข้อความบอกว่าเสร็จแล้ว
    return 'Rice', cook_time  # คืนผลลัพธ์เป็นชื่ออาหารและเวลาที่ใช้

async def cook_noodle():
    cook_time = 1 + random.random()  # กำหนดเวลาทำอาหารแบบสุ่มระหว่าง 1 ถึง 2 วินาที
    print(f"Microwave (Noodle): Cooking {cook_time} seconds...")  # แสดงข้อความบอกเวลาทำอาหาร
    await asyncio.sleep(cook_time)  # หยุดการทำงานตามเวลาที่กำหนดเพื่อจำลองการทำอาหาร
    print("Microwave (Noodle): Finished cooking")  # แสดงข้อความบอกว่าเสร็จแล้ว
    return 'Noodle', cook_time  # คืนผลลัพธ์เป็นชื่ออาหารและเวลาที่ใช้

async def cook_curry():
    cook_time = 1 + random.random()  # กำหนดเวลาทำอาหารแบบสุ่มระหว่าง 1 ถึง 2 วินาที
    print(f"Microwave (Curry): Cooking {cook_time} seconds...")  # แสดงข้อความบอกเวลาทำอาหาร
    await asyncio.sleep(cook_time)  # หยุดการทำงานตามเวลาที่กำหนดเพื่อจำลองการทำอาหาร
    print("Microwave (Curry): Finished cooking")  # แสดงข้อความบอกว่าเสร็จแล้ว
    return 'Curry', cook_time  # คืนผลลัพธ์เป็นชื่ออาหารและเวลาที่ใช้

async def main():
    tasks = [asyncio.create_task(cook_rice()), asyncio.create_task(cook_noodle()), asyncio.create_task(cook_curry())]  # สร้างรายการของงานทำอาหาร
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)  # รอให้งานแรกเสร็จสิ้น

    for task in done:
        dish, time = task.result()  # ดึงผลลัพธ์ของงานที่เสร็จสิ้น
        print(f"Completed task: 1\n - {dish} is completed in {time} seconds")  # แสดงชื่ออาหารและเวลาที่ใช้

    print(f"Uncompleted tasks: {len(pending)}")  # แสดงจำนวนงานที่ยังไม่เสร็จ

# เริ่มโปรแกรม asyncio
asyncio.run(main())
