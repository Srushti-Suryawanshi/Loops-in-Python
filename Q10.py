# Sum of digits

num=int(input("Enter the number :"))
# num=1234
rev=0
sum=0
while num>0:

    digit=num%10
    num=num//10

    sum=sum+digit
    
print(sum)

