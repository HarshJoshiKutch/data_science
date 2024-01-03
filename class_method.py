# class pwskills:
    
#     def __init__(self, name , email): # init for the data pass 
        
#         self.name = name
#         self.email= email
    
#     def students_details(self):
#         print(self.name,self.email)
        
# pw = pwskills("harsh","harsh22@gmail.com") # created object

# print(pw.name)
        
# example -2      

# class pwskills1:
    
#     def __init__(self, name , email): # init for the data pass 
        
#         self.name = name
#         self.email= email
    
#     @classmethod # it is decorator function available in py 
#     def details(cls,name,email):
#         return cls(name,email)
    
#     def students_details(self):
#         print(self.name,self.email)

# pw1 = pwskills1.details("keval","keval@gmail.com")

# print(pw1.name)
# print(pw1.email)

# example - 3

# class pwskills2:
    
#     mobile_num = 9123405432
    
#     def __init__(self, name , email): # init for the data pass 
        
#         self.name = name
#         self.email= email
    
#     @classmethod
#     def change_number(cls,mobile):
#         pwskills2.mobile_num = mobile
    
    
#     @classmethod # it is decorator function available in py 
#     def details(cls,name,email):
#         return cls(name,email)
    
#     def students_details(self):
#         print(self.name,self.email, pwskills2.mobile_num)


# pw = pwskills2.details("rohan","rohan@gmail.com") # means aam je overloading jevu j kaam kare che 
# print(pw.students_details())


# pw_obj = pwskills2("sudh","sudh@gmail.com")
# print(pw_obj.students_details())


# print(pwskills2.change_number(123232323))
# print(pwskills2.mobile_num)

# example - 4

class pwskills3:
    
    mobile_num = 9123405432
    
    def __init__(self, name , email): # init for the data pass 
        
        self.name = name
        self.email= email
    
    @classmethod
    def change_number(cls,mobile):
        pwskills2.mobile_num = mobile
    
    
    @classmethod # it is decorator function available in py 
    def details(cls,name,email):
        return cls(name,email)
    
    def students_details(self):
        print(self.name,self.email, pwskills3.mobile_num)
        
# external function banavyu che and ena help thi pan call karavi sakiye chiye 
def course_details(cls,course_name):
    print("course name is", course_name)

pwskills3.course_details = classmethod(course_details)
print(pwskills3.course_details("data science masters"))

def mentor(cls, list_of_mentor):
    print(list_of_mentor)

pwskills3.mentor = classmethod(mentor)
print(pwskills3.mentor(["sudhanshu","krish naik"]))

# example - 5  change number vadu function delete karva mate del no use thay 

class pwskills4:
    
    mobile_num = 9123405432
    
    def __init__(self, name , email): # init for the data pass 
        
        self.name = name
        self.email= email
    
    @classmethod
    def change_number(cls,mobile):
        pwskills2.mobile_num = mobile
    
    
    @classmethod # it is decorator function available in py 
    def details(cls,name,email):
        return cls(name,email)
    
    def students_details(self):
        print(self.name,self.email, pwskills3.mobile_num)

# method 1 for delete 

del pwskills4.change_number # delete karva mate use thay che 
print(pwskills4.change_number(2343434234)) # means aa karsu to pan aa print thse  AttributeError: type object 'pwskills4' has no attribute 'change_number'

# method 2 for delete

delattr(pwskills4 , "details") # ama deleteattribute no use thay and je function delete karvu che as a string pass kari devanu
print(pwskills4)