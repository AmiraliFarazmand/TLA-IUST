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
import time 
class Grammar():
    def __init__(self,var , products ):
    # var -> products
        self.var = var
        self.products = products    
    def apply_grammar(self,input):
        if self.products=='#':
            input = input.replace(self.var,'')
        else:
            input = input.replace(self.var,self.products)
    @classmethod
    def does_accept(cls,input,string):
        if input.replace(cls.var,cls.products)==string:
            print('Accepted')
            exit()

def 

if __name__ == '__main__':
    grammars_dict = {}
    n=int(input())
    for i in range(n):
        x , y = input().split('->')
        x=x.replace(' ','')
        y=y.replace(' ','')
        y_list = y.split('|')
        for i in y_list:
            temp_grammar = Grammar(x , i)
            grammars_dict[x]= temp_grammar
            
    input_str = input()

    