"""
Implemention of a universal turning machine; check if it accepts a given number tapes or not.

instances :
101101011011001010110101
3

11011011
110111011
>>>
Accepted
Accepted
Rejected
----------------------------------------------------------------
101110110111101100101101111011011001101101101101100110111011011101100110111110111011010011101101110110100111011101110111010011101111010111101100111101101111011011001111010111110101
5
111011111011111111
1111101110111
1110111011111011111

111011111
>>>
Rejected
Rejected
Accepted
Rejected
Accepted
"""

import time
class TuringMachine(object):
    
    def __init__(self, 
                tape = [], 
                initial_state = "",
                final_states = None,
                transition_function = None,
                flag=False,
                blank_symbol='a'
                ):
        
        self.blank_symbol =blank_symbol
        self.__tape = [self.blank_symbol for i in range(5)]+tape+[self.blank_symbol for i in range(5)]
        self.__head_position = 5
        self.__current_state = initial_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)
        self.__flag= flag

    def get_tape(self): 
        return str(self.__tape).replace(' ', '').replace('\'', '').replace(',', '').replace('[', '').replace(']', '')
    
    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            # print('**',self.__tape , self.__head_position ,end='$$')
            # print(x ,y)
            self.__tape[self.__head_position] = y[1] 
            if y[2] == "R":
                self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0]
        if self.final():
            self.__flag = True
        else:
            if self.final():
                self.__flag = True
    @property
    def flag(self):
        return self.__flag
    
    def final(self):
        if self.__current_state in self.__final_states:
            # print('final state:', self.__tape , self.__head_position)
            # print('hooooooooooooooooooooooooora')
            return True
        else:
            return False
'''============================================================================='''
'''============================================================================='''
all_transitions =list( input().split("00") )
states=[]
transitions ={}
for tr in all_transitions:
    elements = list(tr.split("0"))
    start_state = elements[0]
    read_tape = chr(len(elements[1])+96)
    finish_state = elements[2]
    write_tape = chr(len(elements[3])+96)
    move ="L" if elements[4] == "1" else "R"
    if start_state not in states: states.append(start_state)
    if finish_state not in states: states.append(finish_state)

    key_ = (start_state , read_tape)
    Value_ = (finish_state , write_tape , move)
    transitions[key_] = Value_

start_state = "1"
final_states = {max(states)}

ls=[]
n = int(input())
for i in range(n):
    x=[]    
    tstr = input()
    inp = tstr.split('0')
    if tstr.strip():
        for j in inp:
            t = len(j)
            x.append(chr(t+96))
        ls.append(x)
    else:ls.append([])

machines=[]
for tm in range(n):
    tx= TuringMachine(tape =ls[tm],
    blank_symbol ="a",
    initial_state = start_state,
    final_states = final_states,
    transition_function= transitions
    )
    machines.append(tx)

for tx in machines:
    t0=time.time()
    while not tx.final() and time.time()<= t0+0.1:
        tx.step()
    if tx.flag ==True: print('Accepted') 
    else: print('Rejected')
