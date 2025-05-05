# #1
# colors =( "red","green","yellow","black","white")
# print (colors)
# #2
# print(colors[1],colors[4])
# #3
# print(colors[1:4])
# #4
# print("orange" in colors)
# #5
# for color in colors:
#     print(color)
#     ##medium question
# name1=("abe","kebe","bini")
# name2=("yonas","asamn")   
# total=name1+name2
# print(total)
# ##2
# my_number=(1,2,3,1,4,5,1,6,1)
# item=1
# count=my_number.count(item)
# print(f"the item {item} appears {count}times in the tuple")
#3
bracket=("appele", 42, 3.14, "banana", 7)
for x in bracket:
    if type(x) == int():
        print(x)
##hard exercise
#1
def common_item(tuple1, tuple2):
    # Convert the tuples to sets and check if they have any intersection
    return bool(set(tuple1) & set(tuple2))

# Example usage:
tuple1 = (1, 2, 3)
tuple2 = (3, 4, 5)
result = common_item(tuple1, tuple2)
print(result)  # Output: True (since both contain 3)
##2