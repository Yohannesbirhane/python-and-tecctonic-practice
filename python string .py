#string length
text= "how are you ?"
print (len(text))
#check strigs
print("are "in text)
if "we"in text :
    print('yes, "we"  in the text')
else:
    print ('no, " we " in the text')  
    ##slicing string
name="Alemayehu"
print (name[0:])
print(name[:9])
print(name[:4])
print(name[1:5])
#converting case
my_var="hiwot"
print(my_var.upper())
print(my_var.lower())
#replacing string
name="hiwot"
print (name.replace('w','r'))
## string concatination 
first_name="Alemayehu"
last_name="Dems"
full_name=first_name +" " +last_name
print (full_name)
## combining string and numbers
string="Alemayehu"
height=2.5
print (" my name is "+ string +  " and i am " + str(height) +" meter")
print(f"my name is {string},and i am {height} meter")