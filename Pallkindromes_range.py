ans = "y"
while ans != "n":
    num = int(input("enter the number"))
    for i in range(1,num+1):
        if i<10:
            print(i)
        elif i<100 and i%11==0:
            print(i)
        elif i>100:
            r = 0
            while i != 0:
                number = i
                d = number%10
                r = r*10+d
                i = number//10
            if number == i:
                print(i)
    ans = input("press n to stop")