def arithmetic(a: float,b:float,c:str):
    """Lihtne kalkulaato
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetiline tehing
    :rtype var: Märamata tüüb
    """
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c=="/":
        if b!=0:
            r=a/b
        else:
            print("Div0")
            r="Div/0"
    else:
        r="tundmatu sym"
    return r

def is_year_leap(aasta: int):
    """Liigaasta leidmine
    Tagastab true kui aasta on liigaasta ja false kui ei ole 
    :param int aasta: Aastanumber
    :rtype bool: Funktsiooni vastus logilises formaadis
    """
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus

def season(seasondate: int):
   if seasondate==12 or 1<= seasondate <=2:
       print("winter")
   elif  3<= seasondate <=5:
       print("spring")
   elif 6<= seasondate <=8:
       print("summer")
   elif 9<= seasondate <=11:
       print("autunm")
   else:
       print("wrong number")
   return seasondate

from cmath import sqrt


#def prime(number):
#    if number %2==0 and number !=2:
#        return False
#    if number==0 or number==1:
#        return False
#    for n in range(3,int(sqrt(number).real) +1,2):
#        if number %n==0:
#            return False
#    return True

#n = int(input("siseta number  "))
#print(prime(n))
