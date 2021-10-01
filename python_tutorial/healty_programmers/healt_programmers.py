#here we have to build a programme that has to be remind your self for
"""
between 9 to 5
for water - 3.5liter it means 200ml glass has to be done between 9 to 5
   - - 18 glass required to full fill 3500ml water
   --- it means every 45min an ahour you should drink = one glass - -drank
for eye every 30min to do exercise = 16 times -eydone log
for physical every half an hour  = 16 time-exdone log-40min
"""
from datetime import datetime
from pygame import init, mixer 
from time import time



def musicloop(file,stopper):
   mixer.init()
   mixer.music.load()
   mixer.music.play()
   while True:
      a = input()
      if a == stopper:
         mixer.music.stop()
         break

def logno(string):
   with open("mylog.txt","a") as op:
      op.write(f"{string} {datetime.now()}")


if __name__ == "__main__":
   musicloop("water.mp3.mp3","stop")
   # init_water  = time()
   # init_eye = time()
   # init_exercise = time()
   # watersec = 5
   # eyesec = 10
   # exersec = 15

   # if time()-init_water > watersec:
   #    print("water drinking time . enter drank to stop the alarm")
   #    musicloop("water.mp3.mp3", "drank")
   #    init_water = time()
   #    logno("drank water at")





print("welcome to healthy programmer software")


