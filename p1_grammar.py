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
import re
import time 
class Grammar():
    def __init__(self,var , products ):
    # var -> products
        self.var = var
        self.products = products    
    def apply_grammar(self,input_str):
        if self.products=='#':
            input_str = input_str.replace(self.var,'')
        else:
            input_str = input_str.replace(self.var,self.products)
    
def does_accept(cls,input_var,string):
        if input_var.replace(cls.var,cls.products)==string:
            print('Accepted')
            exit()

def derivate(gr:Grammar , inc_string:str ,tmp_string:str='' ):
    tmp_string = tmp_string.replace(gr.var,gr.products)
    does_accept(gr,tmp_string,inc_string)    
    g_list= re.findall(r'^\<..' , tmp_string)
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
    derivate(grammars_list[0][1] , input_str ,grammars_list[0][1].products) 
    derivate(grammars_list[1][1] , input_str ,grammars_list[1][1].products) 
    derivate(grammars_list[2][1] , input_str ,grammars_list[2][1].products) 
    time.sleep(1)
    print('Rejected')
    # print(grammars_list[5][1].products)