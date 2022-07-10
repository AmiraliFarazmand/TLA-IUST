'''
gram_inputs =[
        '<E> -> <E> + <T> | <E> - <T> | <T>' ,
        '<T> -> <T> * <F> | <T> / <F> | <F>' ,
        '<F> -> <F> ^ <G> | sqrt(<G>) | <G>' ,
        '<G> -> ln(<H>) | exp(<H>) | cos(<H>) | sin(<H>) | tan(<H>) | abs(<H>) | <H>' ,
        '<H> -> (<E>) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 '
    ]
    cos(ln(22))
'''
import math 
from time import time
import re
input_str = input()
time0 = time()
flag = True
p_count = 0
'''==============================<<<calculate recursive function>>>============================='''
def calculate(strg:str):
    # only numbers
    print('####', strg ,'####')
    if strg.replace('-' , '').replace('.','').isdigit():
        print('done' ,strg)
        return float(strg)
    # contains ln()
    elif re.search(r'ln\([A-Za-z0-9]*\)', strg):
            part = re.search(r'ln\([A-Za-z0-9]*\)', strg).group()
            print('&&&&' , part)
            x = part[3:-1]
            print('***',x)
            z =calculate(x)
            z = float(z)
            y= math.log (z)
            return strg.replace(part , str(y))
    # contains exp()
    elif re.search(r'exp\([A-Za-z0-9]*\)', strg):
            part = re.search(r'exp\([A-Za-z0-9]*\)', strg).group()
            x = part[4:-1]
            z =calculate(x)
            z = float(z)
            y= math.exp(z)
            return strg.replace(part , str(y))
    # contains abs()
    elif re.search(r'abs\([A-Za-z0-9]*\)', strg):
            # print('***' ,re.search(r'abs\([A-Za-z0-9]*\)', strg))
            part = re.search(r'abs\([A-Za-z0-9]*\)', strg).group()
            x = part[4:-1]
            z =calculate(x)
            z = float(z)
            y= abs(z)
            return strg.replace(part , str(y))
    # contains sin()
    elif re.search(r'sin\([A-Za-z0-9]*\)', strg):
            part = re.search(r'sin\([A-Za-z0-9]*\)', strg).group()
            x = part[4:-1]
            z =calculate(x)
            z = float(z)
            y= math.sin(z)
            return strg.replace(part , str(y))
    # contains cos()
    elif re.search(r'cos\([A-Za-z0-9]*\)', strg):
            part = re.search(r'cos\([A-Za-z0-9]*\)', strg).group()
            x = part[4:-1]
            print('$$$' ,x)
            z =calculate(x)
            z = float(z)
            y= math.cos(z)
            return strg.replace(part , str(y))
    # contains tan()
    elif re.search(r'tan\([A-Za-z0-9]*\)', strg):
            part = re.search(r'tan\([A-Za-z0-9]*\)', strg).group()
            x = part[4:-1]
            print('$$$' ,x)
            z =calculate(x)
            z = float(z)
            y= math.tan(z)
            return strg.replace(part , str(y))
'''============================================================================================'''
try:
    for char in input_str:
        if p_count<0: raise ValueError()
        if char == '(': p_count += 1
        if char == ')': p_count -= 1
    if p_count!=0: raise ValueError() 
    
    # while flag and time() <= time0+0.5 :
    ans =calculate(input_str)
    while not str(ans).replace('-' ,'').replace('.','').replace('(','').replace(')','').isdigit():
        print('answer is:',ans)
        ans2 = calculate(ans)
        ans = ans2
    print ('input is:',input_str, '->' ,ans)
except ValueError :
    print('INVALID')