import abc  # aama thi aapne abstract method lai sakiye chiye 

class pwskills:
    
    @abc.abstractmethod
    def student_details(self):
        pass
    
    @abc.abstractmethod
    def student_assignment(self):
        pass
    
    @abc.abstractmethod
    def student_marks(self):
        pass
    
class student_details(pwskills):
    
    def student_details(self):
        return "this is a method for taking students details"
    
    def student_assignment(self):
        return "this is a method for assigning details for particuler student"
    
    
class data_science_masters(pwskills):
    
    def student_details(self):
        return "this will return student details for data science masters"
    
    def student_assignment(self):
        return "this will give you a stident assignment for data science masters"
    

data_science = data_science_masters() # object create karyu data_Science master nu 
print(data_science.student_details())

student_details = student_details()
print(student_details.student_details())