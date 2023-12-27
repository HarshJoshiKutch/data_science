# a=1
# print(type(a))

# b="harsh"
# print(type(b)) 

# class test :
#     pass

# class test:
#     pass
# a=test()
# print(type(a))

# class fun:
#     def welcome_msg(self):
#         print("welcome to pheonix")
        
# a1 = fun()
# a1.welcome_msg()

class p1:
    def __init__(self,phone_number,email_id,student_id): #constructor tarike use thay  che 
        self.email_id = email_id
        self.phone_number= phone_number
        self.student_id= student_id
        
        def return_student_details(self):
            return self.student_id,self.phone_number,self.student_id 

rohan=p1(123434343,"harsh@gmail.com",121)

print(rohan.phone_number)                                       
 
gaurav= p1(949949494,"gaurav@gmail.com",123)
print(gaurav.phone_number)