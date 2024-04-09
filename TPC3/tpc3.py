import re
import sys


expression = r"(?i)on|off|\d+|="

soma = 0
estado = True

for linha in sys.stdin:
    string = re.findall(expression,linha)

    for elem in string:
        if(elem.lower() == 'off'):
            estado=False
            soma = 0
        if(elem.lower() == 'on'):estado=True
        if(elem[0].isdigit()):
            if(estado==True):soma+=int(elem)
        if(elem == '='):
            print("Resultado:"+str(soma))
            soma = 0
