'''

    tan(cos(sin(22)))
sin(cos(sin(ln(22))))    
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
    strg = strg.replace(' ', '')
    # print('####>', strg ,'<####')
    # only numbers
    if strg.replace('-' , '').replace('.','').isdigit():
        # print('done' ,strg)
        return strg
    # contains ln()
    elif re.search(r'ln\([A-Za-z0-9,.,-]*\)', strg):
            part = re.search(r'ln\([A-Za-z0-9,.,-]*\)', strg).group()
            # print('&&&&' , part)
            x = part[3:-1]
            # print('***',x)
            z =calculate(x)
            z = float(z)
            y= math.log (z)
            return strg.replace(part , str(y))
    # contains exp()
    elif re.search(r'exp\([A-Za-z0-9,.,-]*\)', strg):
            part = re.search(r'exp\([A-Za-z0-9,.,-]*\)', strg).group()
            x = part[4:-1]
            z =calculate(x)
            z = float(z)
            y= math.exp(z)
            return strg.replace(part , str(y))
    # contains abs()
    elif re.search(r'abs\([A-Za-z0-9,.,-]*\)', strg):
            # print('***' ,re.search(r'abs\([A-Za-z0-9]*\)', strg))
            part = re.search(r'abs\([A-Za-z0-9,.,-]*\)', strg).group()
            x = part[4:-1]
            z =calculate(x)
            z = float(z)
            y= abs(z)
            return strg.replace(part , str(y))
    # contains sin()
    elif re.search(r'sin\([A-Za-z0-9,.,-]*\)', strg):
            part = re.search(r'sin\([A-Za-z0-9,.,-]*\)', strg).group()
            # print('op:sin,',part)
            x = part[4:-1]
            z =calculate(x)
            z = float(z)
            y= math.sin(z)
            return strg.replace(part , str(y))
    # contains cos()
    elif re.search(r'cos\([A-Za-z0-9,.,-]*\)', strg):
            part = re.search(r'cos\([A-Za-z0-9,.,-]*\)', strg).group()
            x = part[4:-1]
            # print('$$$' ,x)
            z =calculate(x)
            z = float(z)
            y= math.cos(z)
            return strg.replace(part , str(y))
    # contains tan()
    elif re.search(r'tan\([A-Za-z0-9,.,-]*\)', strg):
            part = re.search(r'tan\([A-Za-z0-9,.,-]*\)', strg).group()
            x = part[4:-1]
            # print('$$$' ,x)
            z =calculate(x)
            z = float(z)
            y= math.tan(z)
            return strg.replace(part , str(y))
    # contains tan()
    elif re.search(r'tan\([A-Za-z0-9,.,-]*\)', strg):
            part = re.search(r'tan\([A-Za-z0-9,.,-]*\)', strg).group()
            x = part[4:-1]
            z =calculate(x)
            z = float(z)
            y= math.tan(z)
            return strg.replace(part , str(y))
    # contains sqrt()
    elif re.search(r'sqrt\([A-Za-z0-9,.,-]*\)', strg):
            part = re.search(r'sqrt\([A-Za-z0-9,.,-]*\)', strg).group()
            x = part[5:-1]
            z =calculate(x)
            z = float(z)
            if z<0: raise ValueError()
            y= math.sqrt(z)
            return strg.replace(part , str(y))
    # contains ()
    elif re.search(r'\([A-Za-z0-9,.,-]*\)', strg):
            part = re.search(r'\([A-Za-z0-9,.,-]*\)', strg).group()
            x = part[1:-1]
            z =calculate(x)
            z = float(z)
            y= z
            return strg.replace(part , str(y))
    # contains ^ case1: ... (... ^ ...) ...
    elif re.search(r'([A-Za-z0-9,.,-]*\^[A-Za-z0-9,.,-]*)', strg):
            part = re.search(r'([A-Za-z0-9,.,-]*\^[A-Za-z0-9,.,-]*)', strg).group()
            splt = part[1:-1].split('^')
            z =calculate(splt[0])
            z2=calculate(splt[1])
            z = float(z)
            z2 = float(z2)
            y= pow(z ,z2)
            return strg.replace(part , str(y))  
    # contains ^ case2: ...(...)...^....(...)...
    elif re.search(r'[A-Za-z0-9,.,-,(,)]*\^[A-Za-z0-9,.,-,(,)]*', strg):
            part = re.search(r'[A-Za-z0-9,.,-,(,)]*\^[A-Za-z0-9,.,-,(,)]*', strg).group()
            splt = part.split('^')
            z =calculate(splt[0])
            z2=calculate(splt[1])
            z = float(z)
            z2 = float(z2)
            y= pow(z ,z2)
            return strg.replace(part , str(y))    
        
    # contains * case1: ... (... * ...) ...
    elif re.search(r'([A-Za-z0-9,.,-]*\*[A-Za-z0-9,.,-]*)', strg):
            part = re.search(r'([A-Za-z0-9,.,-]*\*[A-Za-z0-9,.,-]*)', strg).group()
            splt = part[1:-1].split('*')
            z =calculate(splt[0])
            z2=calculate(splt[1])
            z = float(z)
            z2 = float(z2)
            y= z*z2
            return strg.replace(part , str(y))  
    # contains * case2: ...(...)...*....(...)...
    elif re.search(r'[A-Za-z0-9,.,-,(,)]*\*[A-Za-z0-9,.,-,(,)]*', strg):
            part = re.search(r'[A-Za-z0-9,.,-,(,)]*\*[A-Za-z0-9,.,-,(,)]*', strg).group()
            splt = part.split('*')
            z =calculate(splt[0])
            z2=calculate(splt[1])
            z = float(z)
            z2 = float(z2)
            y= z *z2
            return strg.replace(part , str(y))                       
    # contains / case1: ... (... / ...) ...
    elif re.search(r'([A-Za-z0-9,.,-]*\/[A-Za-z0-9,.,-]*)', strg):
            part = re.search(r'([A-Za-z0-9,.,-]*\/[A-Za-z0-9,.,-]*)', strg).group()
            splt = part[1:-1].split('/')
            z =calculate(splt[0])
            z2=calculate(splt[1])
            z = float(z)
            z2 = float(z2)
            y= z/z2
            return strg.replace(part , str(y))  
    # contains / case2: ...(...).../....(...)...
    elif re.search(r'[A-Za-z0-9,.,-,(,)]*\/[A-Za-z0-9,.,-,(,)]*', strg):
            part = re.search(r'[A-Za-z0-9,.,-,(,)]*\/[A-Za-z0-9,.,-,(,)]*', strg).group()
            splt = part.split('/')
            z =calculate(splt[0])
            z2=calculate(splt[1])
            z = float(z)
            z2 = float(z2)
            y= z/z2
            return strg.replace(part , str(y)) 
        
    # contains + case1: ... (... + ...) ...
    elif re.search(r'([A-Za-z0-9,.,-]*\+[A-Za-z0-9,.,-]*)', strg):
            part = re.search(r'([A-Za-z0-9,.,-]*\+[A-Za-z0-9,.,-]*)', strg).group()
            splt = part[1:-1].split('+')
            z =calculate(splt[0])
            z2=calculate(splt[1])
            z = float(z)
            z2 = float(z2)
            y= z+z2
            return strg.replace(part , str(y))  
    # contains + case2: ...(...)...+....(...)...
    elif re.search(r'[A-Za-z0-9,.,-,(,)]*\*[A-Za-z0-9,.,-,(,)]*', strg):
            part = re.search(r'[A-Za-z0-9,.,-,(,)]*\*[A-Za-z0-9,.,-,(,)]*', strg).group()
            splt = part.split('+')
            z =calculate(splt[0])
            z2=calculate(splt[1])
            z = float(z)
            z2 = float(z2)
            y= z+z2
            return strg.replace(part , str(y))  
    # contains - case1: ... (... - ...) ...
    elif re.search(r'([A-Za-z0-9,.,-]*\-[A-Za-z0-9,.,-]*)', strg):
            part = re.search(r'([A-Za-z0-9,.,-]*\-[A-Za-z0-9,.,-]*)', strg).group()
            splt = part[1:-1].split('-')
            z =calculate(splt[0])
            z2=calculate(splt[1])
            z = float(z)
            z2 = float(z2)
            y= z-z2
            return strg.replace(part , str(y))  
    # contains - case2: ...(...)...-....(...)...
    elif re.search(r'[A-Za-z0-9,.,-,(,)]*\-[A-Za-z0-9,.,-,(,)]*', strg):
            part = re.search(r'[A-Za-z0-9,.,-,(,)]*\-[A-Za-z0-9,.,-,(,)]*', strg).group()
            splt = part.split('-')
            z =calculate(splt[0])
            z2=calculate(splt[1])
            z = float(z)
            z2 = float(z2)
            y= z -z2
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
    
    while not ans.replace('-' ,'').replace('.','').isdigit():#replace('(','').replace(')','').isdigit():
    # while not ans.isdigit():
        ans2 = calculate(ans)
        # print(ans2 ,'\n' ,ans)
        print ('changed:',ans, '->' ,ans2)
        ans = ans2

    # print('@@@final:' , ans)
    print('{0:.2f}'.format(ans))
except ValueError :
    print('INVALID') 
    