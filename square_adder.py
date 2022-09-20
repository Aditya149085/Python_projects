num = int(input("enter a  number"))
num2 = int(input("enter the power"))
if num%2 == 0:
    num =num+1
elif num%2 !=0:
    num = num
else:
    print("wrong input")
total =0
sq=1
for i in range(2,num,2):
    sq=i*i
    total = total+sq
print(total)