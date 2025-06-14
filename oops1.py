#initilize the class
class employee:
    # special method/ magic method/ dunder method -----constructer
    def __init__(self):
        self.id = 123
        self.salary = 60000
        self.designation = "data scientist"
    # creating a method manually
    def travel(self , destination):
        print(f"employee is travelling to {destination}")    

# create an object/instance of the class       
sam = employee()  
# printing the attributes
print(sam.salary)
# calling a method
sam.travel("kerala")

print(type(sam))