items = [int,float,"sandeep",2,5,2,5,2555,222,666,555,1,2,3,4,5,6,]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)