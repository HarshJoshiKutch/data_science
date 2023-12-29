# user ne internal structure ne nai dekhadvanu kaam kare che encapsulation
# __init__ data pass karva mate use thay che 
# class test :
    
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
# t = test(23,24)
# t.a=12345

# print(t.a)

# example - 2

# class car : 
#     def __init__(self,year,make,model,speed): # jya aa bhadha ma __ e private karva mate aapya che 
#         self.__year = year
#         self.__make = make
#         self.__model = model 
#         self.__speed = 0
    
#     def set_speed(self,speed):
#         self.__speed = 0 if speed <0 else speed
    
#     def get_speed(self)  :
#         return self.__speed


# c = car(2021, "toyota","innova",12)

# print(c.__year)  aa private variable che tethi tene pan access nahi kari sakay

# print(c._car__year) #jema aapne acces karva mate class ni aagad _ lagadine karvu padse
# print(c.set_speed(123))
# print(c.get_speed()) # jyare method call karvani hoi tyare 

# exaple - 3:

class bank_account:
    def __init__(self,balance):
        self.__balance = balance
    
    def deposite(self,amount): # aa function banvyo che amount deposite karva mate 
        self.__balance = self.__balance + amount 
        
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__amount = self.__balance - amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.__balance

harsh = bank_account(1000)
print(harsh.get_balance())

print(harsh.deposite(2000))
print(harsh.get_balance())