import requests
import threading
from flask import Flask
from threading import Thread

app=Flask("")
@app.route("/")
def index():
    return ""
Thread(target=app.run,args=("0.0.0.0",8080)).start()

def my_func():
    while True:
        print(requests.get("https://publish.gepro-osi.nl/roosters/rooster.php?klassen%5B%5D=BB1A&klassen%5B%5D=BB2A&klassen%5B%5D=BB2B&klassen%5B%5D=BB2C&klassen%5B%5D=BB3A&klassen%5B%5D=BB3B&klassen%5B%5D=BB3C&klassen%5B%5D=BB4A&klassen%5B%5D=BB4B&klassen%5B%5D=BB4C&klassen%5B%5D=BK1A&klassen%5B%5D=BK1B&klassen%5B%5D=HA2A&klassen%5B%5D=HA2B&klassen%5B%5D=HA2C&klassen%5B%5D=HA2D&klassen%5B%5D=HA3A&klassen%5B%5D=HA3B&klassen%5B%5D=HA3C&klassen%5B%5D=HA3D&klassen%5B%5D=HA3E&klassen%5B%5D=HA4A&klassen%5B%5D=HA4B&klassen%5B%5D=HA4C&klassen%5B%5D=HA4D&klassen%5B%5D=HA4E&klassen%5B%5D=HA5A&klassen%5B%5D=HA5B&klassen%5B%5D=HA5C&klassen%5B%5D=HA5D&klassen%5B%5D=HV1A&klassen%5B%5D=HV1B&klassen%5B%5D=HV1C&klassen%5B%5D=HV1D&klassen%5B%5D=HV1E&klassen%5B%5D=KB2A&klassen%5B%5D=KB2B&klassen%5B%5D=KB2C&klassen%5B%5D=KB2D&klassen%5B%5D=KB2E&klassen%5B%5D=KB3A&klassen%5B%5D=KB3B&klassen%5B%5D=KB3C&klassen%5B%5D=KB3D&klassen%5B%5D=KB3E&klassen%5B%5D=KB4A&klassen%5B%5D=KB4B&klassen%5B%5D=KB4C&klassen%5B%5D=KB4D&klassen%5B%5D=KB4E&klassen%5B%5D=KM1A&klassen%5B%5D=KM1B&klassen%5B%5D=KM1C&klassen%5B%5D=MA2A&klassen%5B%5D=MA2B&klassen%5B%5D=MA2C&klassen%5B%5D=MA2D&klassen%5B%5D=MA3A&klassen%5B%5D=MA3B&klassen%5B%5D=MA3C&klassen%5B%5D=MA3D&klassen%5B%5D=MA4A&klassen%5B%5D=MA4B&klassen%5B%5D=MA4C&klassen%5B%5D=MA4D&klassen%5B%5D=MH1A&klassen%5B%5D=MH1B&klassen%5B%5D=MH1C&klassen%5B%5D=MH1D&klassen%5B%5D=TC2A&klassen%5B%5D=V01A&klassen%5B%5D=VA1A&klassen%5B%5D=VA2A&klassen%5B%5D=VA3A&klassen%5B%5D=VG1A&klassen%5B%5D=VG2A&klassen%5B%5D=VG3A&klassen%5B%5D=VI1A&klassen%5B%5D=VI2A&klassen%5B%5D=VI3A&klassen%5B%5D=VP1A&klassen%5B%5D=VP2A&klassen%5B%5D=VP3A&klassen%5B%5D=VP3B&klassen%5B%5D=VT1A&klassen%5B%5D=VT2A&klassen%5B%5D=VT3A&klassen%5B%5D=VW4A&klassen%5B%5D=VW4B&klassen%5B%5D=VW4C&klassen%5B%5D=VW5A&klassen%5B%5D=VW5B&klassen%5B%5D=VW5C&klassen%5B%5D=VW6A&klassen%5B%5D=VW6B&klassen%5B%5D=VW6C&type=Klasrooster&school=812"))

        
threads = []

for i in range(65):
    t = threading.Thread(target=my_func)
    t.daemon = True
    threads.append(t)

for i in range(65):
    threads[i].start()

for i in range(65):
    threads[i].join()
