num = input ("enter the number")
num_splited = num.split(' 'or',' or', ' or ' ,')
print(num_splited)
max_value=0
for i in range(0,len(num_splited)):
    num_splited[i] = int(num_splited[i])
    if num_splited[i]>max_value:
        max_value = num_splited[i]
    else:
        max_value
print(max_value)