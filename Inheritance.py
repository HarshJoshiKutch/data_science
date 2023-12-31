# Inheritance means je parent class property ne inherit kariye chiye child class ma 

# class test:
#     def test_meth(self):
#         return "this is my first class"

# class child_test(test):
#     pass

# child_test_obj = child_test()

# print(child_test_obj.test_meth())

# there are two types  1: multilevel and 2: multiple inheritance

# multilevel inheritance

# class class1:
#     def test_class1(self):
#         return "this is a method from class1"

# class class2(class1):
#     def test_class2(self):
#         return "this is method form class 2"

# class class3(class2):
#     pass

# obj_class3 = class3() # class3 na object ni help thi pan aapne te bhadhi aagad ni property access kari skaiye chiye

# print(obj_class3.test_class2())


# multiple inheiritence : multiple class mathi access kari sakiye single class ma 

class class1:
    def test_class1(self):
        return "this is a class1"

class class2:
    def test_class2(self):
        return "this is a class2"

class class3(class1,class2):
    pass

obj_class3 = class3()

print(obj_class3.test_class1())
print(obj_class3.test_class2())