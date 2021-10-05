import time
from functools import lru_cache

@lru_cache(maxsize=2)
def calling(data):
    print("hello world:i am lru_cache")
    time.sleep(3)
    
    print(f"your data is this{data}")
    return data

inp = int(input("how many caching you want: "))
if __name__ =="__main__":
    
    print(calling(45))
    input("press any key")
    print(calling(45))
    
   
