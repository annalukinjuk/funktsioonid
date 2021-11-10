from module1 import*
while True:
    print("funktsioonid".center(50, "+"))
    v=input("arithmetic- A")
    if v.upper()=="A":
        arv1=float(input("Arv 1ˇ:"))
        arv2=float(input("Arv 2ˇ:"))
        sym=input("tehe:")
        rezult=aritmethic*(arv1,arv2,sym)
        print(rezult)
    if v.upper()=="Y":
        rezult=is_year_leap(int(input("Siseta aasta: ")))
        print(rezult)