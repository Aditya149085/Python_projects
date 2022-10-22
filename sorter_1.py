ans = "y"
while ans != "n":
    num = input("enter the numbers you want to sort [from -9999999999999 to +9999999999999]")
    list_1 = num.split(' ')
    list_2 = []
    max = -9999999999999
    for i in range(len(list_1)):
        list_1[i] = int(list_1[i])
    for h in range(len(list_1)):
        for i in list_1:
            if i>max:
                max = i
        list_2.append(max)
        list_1.remove(max)
        max = -9999999999999
    list_2 = [*set(list_2)]
    print(list_2)
    ans = input("press n to stop")