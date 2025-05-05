def days_of_week(number):
    match number:
        case 1:
            return " monday"
        case 2:
            return " tuesday"
        case 3:
            return " wendsday"
        case 4:
            return " thursday"
        case 5:
            return " friday"
        case 6:
            return " saturday"
        case 7:
            return " sunday"
        case _:
            return "invalid"
print (days_of_week(1)) 
print (days_of_week(2)) 
print (days_of_week(3)) 
print (days_of_week(4)) 
print (days_of_week(5)) 
print (days_of_week(6)) 
print (days_of_week(7))
print (days_of_week(9))
### 
x=7
y=4
operator="+"
match operator :
    case "+":
        print (f"{x}+{y}={x+y}")
    case "-":
        print (f"{x}-{y}={x-y}")
    case "*":
        print (f"{x}*{y}={x*y}")
    case "/":
        print (f"{x}/{y}={x/y}")
    case "%":
        print (f"{x}%{y}={x%y}")
    case "//":
        print (f"{x}//{y}={x//y}")
        
       
        
    