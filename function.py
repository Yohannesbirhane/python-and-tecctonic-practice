def add_two_numbers (num1,num2):
    sum=num1+num2
    return sum
print(add_two_numbers(34,54))
    
    ##2
def area_of_circle (r):
    PI=3.14
    area=PI*r**2
    return area
print(area_of_circle(6))
##3
def add_all_nums (*values):
    
    return sum(values)
print(add_all_nums(1,2,4))
def convert_celsius_to_fahranite (c):
    fahranite=(c*9/5)+32
    return fahranite 
print(convert_celsius_to_fahranite(5))