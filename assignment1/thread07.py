# Using a ThreadPoolExecutor
import logging
import concurrent.futures
import time

def thread_funtion(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finising", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_funtion, range(3))
