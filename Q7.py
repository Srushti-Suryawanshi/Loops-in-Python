# Factorial using loop

num=int(input("Enter the number :"))
fact=1
for i in range(num):

    fact=fact*(num-i)

print(f"Factorial of {num} is : {fact}")