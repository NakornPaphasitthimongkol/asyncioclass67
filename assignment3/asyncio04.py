# Starting task
from time import ctime
import asyncio

async def wash(basket):
    print(f'{ctime()}   : Washing Machine ({basket}): Put the coin')
    print(f'{ctime()}   : Washing Machine ({basket}): Start washing...')
    await asyncio.sleep(5)
    
