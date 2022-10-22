'''n = int(input(""))
for i in range(0,n+1):
    for j in range(0,i):
        print("*", end ="")
    print("")

n = int(input(""))
count=0
for i in range(0,n+1,2):
    for j in range(0,count+1):
        print(i,end="")
    print("")
    count+=1
    '''
n = int(input(""))
for i in range(0,n+1,2):
    d = i+2
    if i==0 or i>0 and d/i ==2: 
        for j in range(0,i+1,2):
            print(i,end='')
    elif d/i !=2:
        d+=2
    print("")
