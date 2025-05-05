'''colors =["red","white","black","green"]
print (colors)
colros=list(("red","white","black","green"))
print(colors)
print(colors[-2])
## 1 modifing item
## 1.1 add item to the lists
### by using .append() to add item in the last index
colors.append("orange")
print(colors)
colors.insert(2,"blue")
print (colors)
### 1.2 deleting items
##   .pop() :delet the last item 
colors.pop()
print (colors)
## remove(): delet the item by value
colors.remove( "white")
print (colors)
del colors [3]
print (colors)'''
## getting the length of the lists
animals=["cow","goat","sheep","lion"] 
print (len(animals))
## modify an item 
animals [3]="camel"
print (animals)
## check for item 
print("ox " in animals)
## extend the lists 
list1=[ "hailu " "adis","behailu"]
list2=["beti","rahel","mahi"]
list1.extend(list2)
print (list1)
print (list2)
list2.extend(list1)
print(list2)
#Reverse the list 
color =["red", "green", "blue"] 
print (color[-1],color[-2],color[-3])
## Combine the two lists `` and `` into one list.  
a=[1, 2, 3]
b=[4, 5, 6]
a.extend(b)
print (a)
## Modify the list ` by replacing `10` with `12`. 
v=[5, 10, 15]
v[1]=12
print (v)
##Find the length of the list `` and print it.
letters=["a", "b", "c", "d"]
print (len(letters))