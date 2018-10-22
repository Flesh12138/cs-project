def fatrate():
    gender=input("Are you a male or female? If male please input M, if female please input F:")
    while gender!="M" and gender!="F":
        print("Error, please reinput.")
        gender=input("Are you a male or female? If male please input M, if female please input F:")
    height=int(input("Please input height:"))
    neck=int(input("Please input neck circumference:"))
    if gender=="M":
        abdomen=int(input("Please input abdomen circumference:"))
        m1=86.01
        m2=70.041
        m3=36.76
        import math as m
        a=m.log10(abdomen - neck)
        b=m.log10(height)
        fat=m1 * a - m2 * b + m3
    else:
        waist=int(input("Please input waist circumference:"))
        hip=int(input("Please input hip circumference:"))
        f1=163.205
        f2=97.684
        f3=78.387
        import math as m
        c=m.log10(waist + hip - neck)
        d=m.log10(height)
        fat=f1 * c -f2 * d - f3
    print("Your body fat rate is:")
    print(fat)

fatrate()