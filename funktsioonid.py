from module1 import*
from datetime import*
from cmath import sqrt

while True:
    print("funktsioonid".center(50, "+"))
    v=input("arithmetic- A, is year leap - Y, check month season - C, is number prime - P, XOR - X, calculate square features - K, how much money you have - B, is data correct -  D  ")
    if v.upper()=="A":
        arv1=float(input("Arv 1ˇ:"))
        arv2=float(input("Arv 2ˇ:"))
        sym=input("tehe:")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    elif v.upper()=="Y":
        rezult=is_year_leap(int(input("siseta aasta: ")))
        print(rezult)
    elif v.upper()=="K":
        rezult=square(int(input("siseta squaere külk: ")))
        print(rezult)
        print("1 - ümbermõõt, 2 - pindala, 3 - diagonaal")
    elif v.upper()=="C":
        rezult=season(int(input("what month would you like to check?  ")))
        print(rezult)
    elif v.upper()=="P": 
        rezult=is_prime(int(input("Is it true this number is prime? number:   ")))
        print(rezult)
    elif v.upper()=="X":
        rezult=xor_cipher(input("siseta text"),input("siseta võti:"))
        print(rezult)
        de_rezult=xor_uncipher(rezult, input("siseta võti:"))
        print(de_rezult)
    elif v.upper()=="B": 
        money=int(input("money put to bank(vklad) : "))
        yrs=float(input("how many years : "))
        rezult=bank(mnysum)
        print(rezult)
        print("bank account has  ",rezult, " euros" )
    elif v.upper()=="D": 
        rezult=date(int(input("what date you want to check:  ")))
        print(rezult)