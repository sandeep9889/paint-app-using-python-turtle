"""buildin function to reverse"""
# lst = [1,2,3,4,5,6,78,8,9]
# print(lst)
# lst.reverse()
# print(lst)

"""slicing to reverse
"""
# lst1= [123,456,789]
# print(lst1)
# A=lst1[::-1]
# print(A)


"""logical reverse"""

lst = [1,2,3,4,56]
lenght = len(lst) - 1
for item in lst:
    lst[item] = lst[lenght]
    # lenght=-1
