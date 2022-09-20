l = eval(input("you can enter a list within third brackets[x,y,z,..]\nyou can enter tupple whitout brackets(x,y,z...)"))
if isinstance(l,tuple):
    print("tuple")
elif isinstance(l,list):
    print("list")
else:
    print("error")