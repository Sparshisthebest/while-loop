numb=int(input("enter a number: "))
sum=0
temp=numb
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//10
if numb==sum:
    print(numb,"is an armstrong number")
else:
    print(numb,"not a armstrong number")





