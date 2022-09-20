num = int(input("enter a number"))
factors = 0
factor = 0
for i in range(1,num+1):
    if num%i == 0:
        factors = factors+1
        factor = 1
        print(i)
if factors == 2:
    print("prime number")
elif factors < 1:
    print("it has only one factor")
else:
    print("composite number")