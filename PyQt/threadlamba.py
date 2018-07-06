from threading import Thread
import urllib.request
import random
t = Thread()

t.run = lambda : print("HELLO VOID")

#print("BOSS IS BOSS")
url = "https://download.gtanet.com/gtagarage/files/image_70116.jpg"


for i in range(10):
    fname = str(i) + url.split("/")[-1]
    Thread(target=lambda : urllib.request.urlretrieve(url,fname)).start()