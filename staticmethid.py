# class pwskills :
    
#     def student_details(self, name , mail_id , number):
#         print(name , mail_id , number )

# pw = pwskills() # created object

# print(pw.student_details("harsh", "harsh2@gmail.com", 9106683737))

# example 2: static method decorator jema directly class na name thi pan access kari sakay che 

# class pwskills1 :
    
#     def student_details(self, name , mail_id , number):
#         print(name , mail_id , number )
        
#     @staticmethod
#     def mentor_class(list_mentor):
#         print(list_mentor)
        
#     def mentor(self,mentor_list):
#         print(mentor_list)
        
# print(pwskills1.mentor_class(["krish","sudh"]))

# # jya stu1 e function copy create kare che 
# stu1 = pwskills1()
# stu2 = pwskills1()
# stu3 = pwskills1()

# example 2

class pwskills2 : #class method ni under static method call kari sakay che 
    
    def student_details(self, name , mail_id , number):
        print(name , mail_id , number )
        
    @staticmethod
    def mentor_mail_id(mail_id_mentor):
        print(mail_id_mentor)
    
    @staticmethod
    def mentor_class(list_mentor):
        pwskills2.mentor_mail_id("sudh@gmail.com") # ek static ni under biji static method call kari che 
        print(list_mentor)
   
    
    @classmethod
    def class_name(cls):
        cls.mentor_class(["krish","sudh"])
        
        
    def mentor(self,mentor_list):
        print(mentor_list)
        
# print(pwskills2.class_name())


print(pwskills2.mentor_class(["anoop","babbar"])) # aa static ma static call karva mate use thay 