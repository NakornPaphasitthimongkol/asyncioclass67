import time
import asyncio

judit_compute = 0.1
opponent_compute = 0.5
opponent = 3
move_board = 30

async def main(i):

    start_board = time.perf_counter()

    for j in range(move_board):
        time.sleep(judit_compute)
        print(f"Board {i}-{j} Judit make move.")
        await asyncio.sleep(opponent_compute)
        print(f"Board {i}-{j} Opponent make move.")
    
    end = time.perf_counter() - start_board
    print(f'{time.ctime()} - Board {i} finish in ', end, "seconds." )
        

async def game_task():
    start_game = time.perf_counter()
    tasks = []
    for i in range(opponent):
        tasks.append(main(i))

    await asyncio.gather(*tasks)
    end_game = time.perf_counter() - start_game
    print(f'{time.ctime()} - All board done in ', end_game, "seconds." )

if __name__=="__main__":
    asyncio.run(game_task())