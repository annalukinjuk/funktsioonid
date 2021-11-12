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

def square(ruud: float):
    """kvadrati leidimine
    küsib külk, tagastab ümbermõõt, pindala ja diagonaal
    :param int side: külk
    :rtype bool: square tagastab logilises formaadis
    """
    return(4*kv, kv**2, (2*kv**2)**.5)

def season(seasondate: int):
    """Sesooni leidimińe, tagastab nimi sesooni ja wrong number kui else
    :param int seasonsdate: Sesooni date
    :rtype var: funktsiooni vastus sesooni formadis
    """
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

def is_prime(number: int):
    """priim numbri leidmine
    Tagastab true kui number on kerge, tahastab false kui élse.
    :param int number: number
    :rtype bool: Funktsiooni vastus logilises formaadis
    """
    b=2
    while number%b!=0:
        b+=1
    return b==number
    if number %2==0 and number !=2:
        return False
    if number==0 or number==1:
        return False
    for number in range(3,int(sqrt(number).real) +1,2):
        if number %n==0:
            return False
    return True

def bank(a:float, years:int):
    """Banki raha ja aasta leidimine
    Tagastab raha tulevad banki
    :param int money: money that customer put to bank acc
    :param float: how many aastat
    :rtype var: money sum
    """
    for y in range(1,yrs+1):
        percentcalc=money1*0.10
        mnysum=money1+percentcalc
    return mnysum

def date(day: int, month: int, year: int):
    """Leidimine kui date exists või see on vale data number
    Tagastab true kui data number on meie kalendris false kui ei ole
    :param int data: number
    :rtype bool: Funktsiooni vastus logilises formaadis
    """
    def date(day:int, month:int, year:int):
      set_months = {1: 31,2: 28, 3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31}
    if year>0 and (month>=1 and month<=12):
        if day in range(1, set_months[month]+1):
           return True
        else:
            return False
def xor_cipher(string: str, key:str)->str:
    """Tavaline sõna kodeeritakse
    """
    result=''
    temp=int()
    for i in range(len(string)):
        temp=ord(string[i]) #näitab sümboli kood
        for j in range(len(key)):
            temp^=ord(key[j])
        result+=chr(temp)
    return result
def xor_uncipher(string: str, key: str)->str:
    """kodeeritud text dekoreeritakse
    """
    result=''
    temp=[]
    for i in range(len(string)):
        temp.append(string[i])
        for j in reversed(range(len(key))):
            temp[i]=chr(ord(key[j]))^ord(temp[i])
        result+=temp[i]
    return result