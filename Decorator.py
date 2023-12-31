# def test():
#     print("this is the start of my function")
#     print("this is my function to test")
#     print(4+5)
#     print("this is the end of my function")
    
# print(test())

#jya aapne aa start and end valu repeatedly lakvu pade che je aapne na lakhvu pade te mate aa use kariye chiye 

# example-1

# def deco(func):
#     def inner_dec():
#         print("this is the start of my function")
#         func()
#         print("this is the end of my function")
#     return inner_dec


# @deco # jya je call karavanu che funtion ni upwer aa lagadvathi te uper na function par jai ne e ni sathe first call kare che 
# def test1():
#     print(6+7)

# print(test1())

# example 2: time packege ma start and end time hoi 

import time

def timer_test(func):
    def timer_test_inner():
        start = time.time() # atyarnu je time hase e dekhadva mate 
        func()
        end = time.time() 
        print(end - start)
    return timer_test_inner


# @timer_test # jya @ lagadine karvathi aapne je uper aapela function ne use kari sakiye chiye 
# def test2():
#     print(40+20)

# print(test2())

#example-3  ek functin ne execute thata ketlo time lage che e check karva mate

@timer_test
def test():
    for i in range(100000):
     pass

print(test())
