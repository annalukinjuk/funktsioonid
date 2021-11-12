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
    if number %2==0 and number !=2:
        return False
    if number==0 or number==1:
        return False
    for number in range(3,int(sqrt(number).real) +1,2):
        if number %n==0:
            return False
    return True

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