def arithmetic(a: float,b:float,c:str):
    """Lihtne kalkulaato
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetiline tehing
    :rtype float:
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
            r=0.0
    else:
        print("viga")
        r=0.0
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