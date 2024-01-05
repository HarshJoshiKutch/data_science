# example - 1

# try:
#     a = 10/0
# except ZeroDivisionError as e:
#     print(e)

# example - 2

# try :
#     int ("sudh")
# except (ValueError , TypeError) as e:
#     print(e)

# example - 3 this will catch the error 

# try :
#     int ("sudh")
# except :
#     print("this will catch an error")
    
# example - 4

# try :
#     import harsh
# except ImportError as e:
#     print(e)
    
# example - 5

# try :
#     d = {"key:sudh","key:harsh"}
#     print(d["key2"])
# except KeyError as e:
#     print(e)

# example - 6

# try :
#     "harsh".test()  
# except AttributeError as e:
#     print(e)

# example - 7

# try :
#     l = [2,3,4,5]
#     print(l[6])
# except IndexError as e:
#     print(e)

# example - 8
try:
    with open("text.txt",'r') as f:
        test = f.read()
except FileNotFoundError as e:
    print(e)
    
dir(Exception)