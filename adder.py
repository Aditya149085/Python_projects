again = "y"
while(again =="y"):
    num = input("enter the number you want to add")
    num_splited = num.split(' ')
    print(num_splited)
    decision = input("do you want to change the values?")

    if decision == "y":
        repeat = "y"
        while(repeat == "y"):
            changed_value_num = int(input("which value you want to change?"))
            changed_value = input("To what do you want to change?")
            changed_value_num-=1
            num_splited[changed_value_num] = changed_value
            repeat = input("do you want to repeat? [y/n]")


    if repeat == "n":
        print("adding all values....")
        total = 0
        for i in range(0,len(num_splited)):
            num_splited[i] = int(num_splited[i])
            total = total+num_splited[i]
        print("result = ",total)
    again = input("again?[y/n]")