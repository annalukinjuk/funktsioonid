from module1 import*
from datetime import*
from cmath import sqrt

while True:
    print("funktsioonid".center(50, "+"))
    v=input("arithmetic- A, is year leap - Y, check month season - C ")
    if v.upper()=="A":
        arv1=float(input("Arv 1ˇ:"))
        arv2=float(input("Arv 2ˇ:"))
        sym=input("tehe:")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    if v.upper()=="Y":
        rezult=is_year_leap(int(input("siseta aasta: ")))
        print(rezult)
    if v.upper()=="C":
        rezult=season(int(input("what month would you like to check?  ")))
        print(rezult)
    if v.upper()=="P":
        rezult=