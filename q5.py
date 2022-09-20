num = input ("enter the numbers you want to add")
num_splited = num.split(' ')
print(num_splited)

dicision_result = input("do you want to change it? [y/n]")
if dicision_result== "y":
    changed_value_num = input("what value you want too change?")
    changed_value_num-1
    changed_value = input("what do you want to change?")
    num_splited[changed_value_num] = changed_value

elif dicision_result== "n":
    print("ok no problem")
print("adding all values")
total = 0
for i in range(0, len(num_splited)):
    num_splited[i] = int(num_splited[i])
    total = total + num_splited[i]
print(total)