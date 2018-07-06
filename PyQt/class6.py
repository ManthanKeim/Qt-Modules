import time
import threading

name1 = str(input())

name2 = str(input())


def download(txt):
    for i in range(5):
        time.sleep(1)
        print("WE HAVE DOWNLOAD" , i+1 , "of " , txt)

class worker(threading.Thread):

    def __init__(self, namea):
        super().__init__()
        self.namea = namea

    def run(self):
        download(self.namea)

w1 = worker(name1)
w2 = worker(name2)

w1.start()
w2.start()

print("DONE")

for item in threading.enumerate():
    print(item.name)