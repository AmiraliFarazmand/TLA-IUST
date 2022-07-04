'''
Determine whether the given grammar accepts the input or not.
instances:
3
<S> -> a<S>b | a<A> | b<B>
<A> -> a<A> | #
<B> -> b<B> | #
aaab
    >>>Accepted
------------------------------------------------------------------------------
4
<S> -> <S>a | <S>b | <A>a | <B>b
<A> -> ab<A> | <B>ca | #
<B> -> b<B> | <C>f
<C> -> a<C> | #
abbfcaba
    >>>Rejected
'''
from dataclasses import replace
import re
import time

from pyrsistent import inc 
class Grammar():
    def __init__(self,var , products ):
    # var -> products
        self.var = var
        self.products = products    
    def apply_grammar(self,input_str):
        if self.products=='#':
            input_str = input_str.replace(self.var,'')
            return input_str
        else:
            input_str = input_str.replace(self.var,self.products)
            return input_str
    # def does_accept(self,input_var,string):
    #     if input_var.replace(self.var,self.products)==string:
    #         print('Accepted')
    #         exit()
    #     else:
    #         pass

def derivate(gr:Grammar , inc_string:str ,tmp_string:str='' ):
    if gr.apply_grammar(tmp_string)==inc_string:
        print('Accepted')
        exit()
    else:
        # tmp_string = tmp_string.replace(gr.var,gr.products)
        tmp_string = gr.apply_grammar(tmp_string)
        g_list= re.findall(r'<[A-Za-z]*>', tmp_string)
        if len(tmp_string)<=len(inc_string)+6 and g_list!=[]:
            if tmp_string==inc_string: print('***didnt work',tmp_string,g_list)
            for g in g_list:
                for i in grammars_list:
                    if i[0] == g:
                        gram = i[1]
                        derivate(gram,inc_string,tmp_string) 
    

if __name__ == '__main__':
    grammars_list =[]
    n=int(input())
    for i in range(n):
        x , y = input().split('->')
        x=x.replace(' ','')
        y=y.replace(' ','')
        y_list = y.split('|')
        for i in y_list:
            temp_grammar = Grammar(x , i)
            grammars_list.append([x ,  temp_grammar ])
            
    input_str = input()
    time0=time.time()

    for g in grammars_list:
        derivate(g[1] , input_str ,'<S>')
    time.sleep(1)
    print('Rejected')
    
    