# extending the Thread class and return values
from time import sleep, ctime
from threading import Thread

class CustomThread(Thread):
    def run(self):
        sleep(1)
        print(f'{ctime()} This is from another thread')
        self.value = 99

thread = CustomThread()

thread.start()

print(f'{ctime()} Waiting for the thread...')
thread.join()

value = thread.value
print(f'{ctime()} Got: {value}')
