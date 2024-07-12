import asyncio
from random import random

# coroutine เพื่อทำอาหารแต่ละจาน
async def cook_dish(dish_name):
    time_to_cook = 1 + random()
    await asyncio.sleep(time_to_cook)
    print(f'{dish_name} is done in {time_to_cook:.2f} seconds')

# coroutine หลัก
async def main():
    # สร้าง task สำหรับทำอาหารแต่ละจาน
    dishes = ['rice', 'noodle', 'curry']
    tasks = [asyncio.create_task(cook_dish(dish)) for dish in dishes]
    
    # รอให้ทุก task เสร็จสมบูรณ์
    done, pending = await asyncio.wait(tasks)
    
    # รายงานผลลัพธ์
    for task in done:
        print(task.result())

# เริ่มโปรแกรม asyncio
asyncio.run(main())
