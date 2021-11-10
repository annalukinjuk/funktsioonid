#while True:
#    print("funktsioonid")

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
    elif c==