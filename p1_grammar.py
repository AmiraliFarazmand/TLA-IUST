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
------------------------------------------------------------------------------
4
<E> -> <E>+<T> | <E>-<T> | <T>
<T> -> <T>*<F> | <T>/<F> | <F>
<F> -> <F><G> | <G>
<G> -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
42+56/8125442
-----------------------------------------------------------------------------
4
<E> -> <E>+<T> | <E>-<T> | <T>
<T> -> <T>*<F> | <T>/<F> | <F>
<F> -> <F><G> | <G>
<G> -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
30+-71111
------------------------------------------------------------------------------
4
<E> -> <E>+<T> | <E>-<T> | <T>
<T> -> <T>*<F> | <T>/<F> | <F>
<F> -> <F><G> | <G>
<G> -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
15*9
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
            return input_str
        else:
            input_str = input_str.replace(self.var,self.products)
            return input_str

def derivate(gr:Grammar , inc_string:str ,tmp_string:str='' ):
    tmp_string = gr.apply_grammar(tmp_string)
    if tmp_string == inc_string:
        print('Accepted')
        quit()
    else:
        # tmp_string = tmp_string.replace(gr.var,gr.products)
        g_list= re.findall(r'<[A-Za-z0-9]*>', tmp_string)
        # if tmp_string==inc_string: print('***didnt work',tmp_string,g_list)
        if len(tmp_string)<=3*len(inc_string):
            for g in g_list:
                for i in grammars_list:
                    if i[0] == g:
                        if list([i[1], tmp_string]) not in visited_situations:
                            if '<' in i[1].products:
                                gram = i[1]
                                print('*****' ,tmp_string , ';' ,gram.var , '->' ,gram.products)
                                derivate(gram,inc_string,tmp_string) 
                                visited_situations.append(list([i[1], tmp_string]))
                            else:
                                gram = i[1]
                                derivate(gram,inc_string,tmp_string) 
                                visited_situations.append(list([i[1], tmp_string]))
        else:
            pass
        

if __name__ == '__main__':
    grammars_list =[]
    visited_situations = [] #prevents grom getting into loops
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

    for g in grammars_list :
        # if time.time()<= time0+1.5:
        # for iv in grammars_list:
            # derivate(g[1] , input_str , iv[0])
            derivate(g[1] , input_str , grammars_list[0][0])
    
    # time.sleep(0.5)
    print('Rejected')
    # print(*visited_situations ,sep='\n')
    