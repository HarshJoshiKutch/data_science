# l=[2,3,4,5,6]
# def test(l):
#     l1=[]
#     for i in l:
#         l1.append(i**2)
#     return l1
# print(test(l))

# uper na j function nej apde ap vade easily solve kari sakiye

# l=[2,3,4,5,6]

# def sq(x):
#     return x**2
# print(list(map(sq,l)))

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# print(list(map(lambda x,y:x+y,l1,l2)))

# s=("harshjoshi")
# print(list(map(lambda s:s.upper(),s)))

 #//new function
# from functools import reduce
# l=[1,2,3,4,5,6,3]
# print(reduce(lambda x,y:x+y,l))

# print(reduce(lambda x,y: x*y,l))

# print(reduce(lambda x,y: x if x>y else y,l))

# Filter function

# print(list(filter(lambda x: x%2==0,l)))
# print(list(filter(lambda x: x%2==0,l)))

#// new function

l1=["harsh","keval","dhruv","nand","nandish"]
print(list(filter(lambda x:len(x)<6 ,l1)))

