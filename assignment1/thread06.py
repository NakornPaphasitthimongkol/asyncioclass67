# Working With Many Threads
import logging
import threading
import time

def thread_funtion(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finising", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    
    thread = list()
    for index in range(3):
        logging.info("Main  :create and start thread %d.", index)
        x = threading.Thread(target=thread_funtion, args=(index,))
        thread.append(x)
        x.start()


    for index, thread in enumerate(thread):
        logging.info("Main  :before joining thred%d.", index)
        x.join()
        logging.info("Main  :thread %d done", index) 
        
