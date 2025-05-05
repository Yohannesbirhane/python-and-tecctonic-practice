# if statement
#write a program tocheck the given number is positive
# '''num=int(input('enter the number'))
# if num>0:
#     print(num ,'is positive')
# if num <0:
#     print(num ,'is negative')'''    
    # largest from three numbers
'''a=int(input( 'enter  a'))
b=int (input ('enter  b'))
c=int(input ('enter  c'))
if a>b>c:
    print(a ,'is greater than ',b  and c)

    print (bool(a>b>c))  '''  
    # if _else statement
 # check the number is even or not
"""p=int (input('enter the value '))
if p%2==0:
    print(p ,'is even')
else:
    print (p,'is odd')"""    
    #elif statement
"""mid=int( input ( 'enter mid value '))
final=int (input ('enter final value'))
total_mark=mid+final
if total_mark>=90 and  total_mark <=100:
    print ('your grade is  A+')
elif total_mark>=85 and  total_mark<90:
    print ('your grade is A')
elif  total_mark>=80:
    print ('your grade is A-')
elif total_mark >=75:
    print ('your grade is B+')
else:
    print ('your grade is D')"""
    # loop in python
    #for loop
'''sum=0
for f in range  (1,101,1):
    sum+=f
print ('the sum is',sum)    '''
#######)) the no divisible by 2and 5
    
'''a=int (input( "enter the number"))
if a%2==0:
    print (a,"is divisible by 2")
    if a%5==0:
        print (a,'is divisible by 5')
    else:
        print  (a,'is not divisible by 5')   
else:
    print (a,'is not diviible by 2')
    if a%5==0:
        print (a,'is divisible by 5')
    else:
        print(a,'is not divisible by 5')'''
'''modify item
run=["banana","orange","lemon","apple","avocado"]
print(run)
y=["appele ","banana","cherry"]
print(y[2])
x=["appele ","banana"]
x.append("kiwi")
print(x)
x.remove("banana")
print (x)
lists=["cat","dog","fish"]
for i in lists:
    print(i)
    '''

'''''
x=[
  [1,2,3],
  [2,3,4],
  [1,2,3]
  ]
print(x[1])'''
# ## write aprogram to check whether a number is positive ,negative ,or  zero 

# num=int(input ("enter the number"))
# if num>0:
#      print(f"{num} is positive")
# elif num <0:
#     print (f"{num} is negative")
# else:
#     print(f"{num} is zero")
'''    # Create a program that prints "Eligible to vote" if the age is 18 or above, otherwise prints "Not eligible."
while True:
 age =int(input ("enter the age "))
 print ("Eligile to vote")if age>=18 else  print('Not eligible')'''
#   # Write a nested `if` program to check whether a number is divisible by 2 and also by 5.
# number=int(input("enter the number"))
# if number %2==0:
#     print(number ,"is divisible by 2")
#     if number %5==0:
#         print ("and also divisible by 5")
#     else:
#         print(number, "is divisible by only 2 ") 
## electrical payment  
watt =int (input ( "enter the watt"))
if watt>0 and watt<=100:
  print (f"you should pay 50 birr")
elif watt>100 and watt<=300:
  print (f"you should pay 100 birr")
elif watt>300 and watt<=600:
  print (f"you should pay 150 birr")
elif watt>600 and watt<=900:
  print (f"you should pay 200 birr")
else:
  print (f"you should pay  600 birr") 