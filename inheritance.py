#Create a Person class and a Student class that inherits it.
# Add an id attribute to Student
class person :
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    def __str__ (self):
        return f" name: {self.name} ,age: {self.age}"
class student(person):
    def __init__(self, name,age ,student_id ):
        super().__init__(name, age)
        self.student_id=student_id
    def __str__(self):
        return f"name :,{self.student_id}"
person1=person("yishaq" ,43)
student2=student("yohannes" ,46 ,"DBU1601767")
print(person1)
print(student2)
##Create a Vehicle class with a method fuel_efficiency() 
# and override it in Car and 
# Bike subclassef"
        