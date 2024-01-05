# age = int(input("enter your age"))

class validateage(Exception):
    def __inti__(self,msg):
        self.msg = msg

def validateage(age):
    if age<0:
        raise validateage("entered age is negative ") # exception ne raise kari dese
    elif age>200:
        raise validateage("enterd age is very very high")
    else :
        print("age is valid")

try:
    age = int (input("enter your age"))
    validateage(age)
except validateage as e :
    print(e)