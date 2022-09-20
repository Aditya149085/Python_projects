tempreture_unit = input("ent5er the unit of the tempreture [c/f]")
if tempreture_unit == "c" or tempreture_unit == "C":
    tempreture_c = float(input("enter the tempreture"))
    tempreture_f =((tempreture_c/5)*9)-32
    print("Tempreture in ferenheit ",tempreture_f,"F")
elif tempreture_unit == "f" or tempreture_unit == "F":
    tempreture_f = float(input("enter the tempreture"))
    tempreture_c =((tempreture_f-32)*5)/9
    print("tempreture in celcius ",tempreture_c,"C")
else:
    print("wrong input")