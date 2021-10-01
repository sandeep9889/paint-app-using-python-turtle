#checking time of for loop and while loop
import time
initial = time.time() #it give some ticks ticks  are second
i=1
while(i<45):
    print("sandeep bhai ki jai")
    i+=1
print("the time for while loop:",{time.time()}-{initial},"seconds" )    

initial1 = time.time()
for i in range (45):
    print("sandeep bhai ki jai")

print("the time for for loop:", {time.time()}-{initial1},"seconds" ) 

localtime = time.asctime(time.localtime(time.time()))
print(localtime)