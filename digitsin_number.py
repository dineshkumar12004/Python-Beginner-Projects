# To count number of digits in the given number 

number = int(input("Enter a number: "))
count = 0
while(number > 0):
    number = number//10
    count = count + 1
print("The number of digits in the number are: ",count)