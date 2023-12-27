# multiple kind of behaviour in a diffrent kind of situation  poly etle multilple behavior
def test(a,b):
    return a+b
print(test(2,3))

print(test("harsh","joshi")) 

# passing the list in function
print(test([3,4,5,6],[45,456,221]))


class data_science:
    
    def syllabus(self):
        print("This is my syllabus for data science masters")

class web_dev:
    
    def syllabus(self):
        print("this is my syllabus for web dev")

def class_hj(class_obj):
    for i in class_obj:
        i.syllabus()    
# create an objects for datascience and webdev

data_science = data_science()
web_dev = web_dev()
class_obj = [data_science,web_dev]

print(class_hj(class_obj))


# for exmaple mate you can give you are a person with at diffrente places you can work with others life employes , family person, friend