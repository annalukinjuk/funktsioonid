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

#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
a = tuple()
a = (1,2,3,4,5,6,7,8,9,10,11,12)