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
            number = i
            while number > 0:
                d = number%10
                r = r*10+d
                number = number//10
            if r == i:
                print(i)
            else:
                None
    ans = input("press n to stop")