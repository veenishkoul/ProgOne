# python script to print string of number in series

var1 = ''
print("Enter any interger :")
n = int(input())

for x in range(1,n+1):
    var1 = str(var1) + str(x)
print(var1)

