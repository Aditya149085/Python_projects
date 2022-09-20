start_value = int(input("give the starting value"))
ending_value = int(input("give a ending value"))+1
total = 0
if start_value <ending_value:
    for i in range(start_value,ending_value):
        total = total+i
    print(total)
else:
    print("wrong input")
