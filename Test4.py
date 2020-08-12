# python script to print string of number in series

var1 = ''
print("Enter any interger :")
n = int(input())
for x in range(1,n+1):
    var1 = str(var1) + str(x)
print(var1)

###########To check list logic##########
list1 = [2,6,3]
print(5 not in list1)
if(5 not in list1):
 print("5 not in list1")

#####TO test age for driving########

print("what is your age")
age = int(input())
if (age > 7 and age < 100):
    if age < 18:
        print("you cannot drive")
    elif age == 18:
        print("we will see")
    else:
        print("you can drive")
else:
    print("Enter valid age")

