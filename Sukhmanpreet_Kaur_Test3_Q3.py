sum = 0
n= int(input("Enter the ending number: "))

for num in range(1,n+1,1):
    sum = sum+num
print("The sum of the first ",n," numbers is : ", sum)
average = sum/n
print("The average of the first ",n, "number is: ", average)