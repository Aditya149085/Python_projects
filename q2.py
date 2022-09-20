name = input("enter your name student")
marks_eng = float(input("enter your marks in eng."))
marks_math = float(input("enter your marks in math."))
marks_phy = float(input("enter your marks in phy."))
marks_chem = float(input("enter your marks in chem."))
marks_cs = float(input("enter your marks in C.S."))
#q2.5 start
if marks_eng>70 or marks_math>70 or marks_phy>70 or marks_chem>70 or marks_cs>70:
    print("you entered wrong marks in one or more of your subjects")
#q2.5 end
else:
    total_marks = marks_eng+marks_math+marks_phy+marks_chem+marks_cs
    percent = ((total_marks)*100)/350
    average_marks = (total_marks)/5
    is_passed =""
    if percent >= 33:
        is_passed = "You passed"
    else:
        is_passed = "You failed"
    print(name," your percentage is = ",percent,"% Your total marks is = ",total_marks,"your average marks is ",average_marks,is_passed)
