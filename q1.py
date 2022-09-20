ab = float(input("enter the number"))
a = int(ab)
if a%2==0 & a%5==0:
    print("even number,multiple of 5")
elif a%2==0 & a%5!=0:
    print("even number,not multiple of 5")
elif a%2!=0 & a%5==0:
    print("ood number,multiple of 5")
else:
    print("odd number,not a multiple of 5")
