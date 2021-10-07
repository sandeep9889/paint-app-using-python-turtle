# corutlines used if u wNANT TO import machine lerning module like it take some times but if you want to run something in a code when one thing takes time
def names():
    import time
    names = "akash harry haris carry amit ajey bhuvan shubham rahul aftab hrithik vivek ujjawal mohit rohit"
    time.sleep(2)

    while True:#from here if you want run this loop then we have to use corutline
        text = (yield)
        if text in names:
            print("Your name is in the list.")
        else:
            print("Your name is not in the list.")

name = names()
next(name)

name.send(input("Type your Name: "))
name.send(input("Type your Name: "))

name.close()

