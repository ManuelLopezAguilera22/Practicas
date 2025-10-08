
from math import floor, ceil



def parte_fraccionaria(a:float)-> float :
    if (a>=0):
        pe = floor(a)
        ret= a-pe
    else:
        pe=ceil(a)
        ret= a-pe
    return ret

def redondea(a:float, n:int)-> float:
    return  round(a, n)
    
def eliminar_espacios_sobrantes (a: str)-> str:
    return " ".join(a.split())

def detectar_isograma (a:str)-> bool:
    a=a.lower()
    for i in a:
        if a.count(i)>1 and i.isalpha():
            return False
    return True


def transformar_en_camelcase(a:str)-> str:
    a = eliminar_espacios_sobrantes(a)
    a = a.title()
    a = a.replace(" ", "")
    if len(a) > 0:
        a = a[0].lower() + a[1:]
    return a
