# pickleing a file  
import pickle
# cars = ["audi","bmw","maruti suzuki"]
# file = "mycar.pkl"
# fileobj = open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()
file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)