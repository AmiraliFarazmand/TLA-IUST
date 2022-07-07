from asyncore import read
from textwrap import wrap
import time
from tokenize import blank_re
from typing import final


class TuringMachine(object):
    
    def __init__(self, 
                tape = [], 
                initial_state = "",
                final_states = None,
                transition_function = None,
                flag=False,
                blank_symbol=''
                ):
        
        self.__tape = ['#' for i in range(5)]+tape+['#' for i in range(5)]
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
        self.blank_symbol =blank_symbol

    def get_tape(self): 
        return str(self.__tape).replace(' ', '').replace('\'', '').replace(',', '').replace('[', '').replace(']', '')
    
    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            print('**',self.__tape , self.__head_position ,end='$$')
            print(x ,y)
            self.__tape[self.__head_position] = y[1] 
            if y[2] == "R":
                self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0]
        # if self.final():
        #     self.__flag = True
        else:
            if self.final():
                self.__flag = True
    @property
    def flag(self):
        return self.__flag
    def final(self):
        if self.__current_state in self.__final_states:
            print('final state:', self.__tape , self.__head_position)
            return True
        else:
            return False
'''============================================================================='''
'''============================================================================='''
# initial_state = "init",
# accepting_states = ["final"],
# transition_function = { ("init","0"):("init", "0", "R"),
#                         ("init","1"):("init", "0", "R"),
#                         ("init","0"):("final","1", "L")
#                         }
# final_states = {"final"}

# t = TuringMachine(list("10"), 
#                     initial_state = "init",
#                     final_states = final_states,
#                     transition_function=transition_function,
#                     flag=False,
#                     blank_symbol='1')

# print("Input on Tape:\n" + t.get_tape())
# # age state aval final bashe handle nemishe!!!!
# t0=time.time()
# while not t.final() and time.time()<= t0+1:
#     t.step()

# if t.flag==True: print('Accepted')
# # print("Result of the Turing machine calculation:")    
# print(t.get_tape())
print('====================================================================================================')
# all_transitions =list( input().split("00") )
all_transitions = list('101101011011001010110101'.split("00"))
states=[]
transitions ={}
for tr in all_transitions:
    elements = list(tr.split("0"))
    start_state = elements[0]
    if elements[1] =='1': read_tape = 'a' 
    if elements[1] =='1': read_tape = 'a' 
    if elements[1] =='111': read_tape = 'c' 
    finish_state = elements[2]
    if  elements[3] =='1': write_tape= 'a'
    if  elements[3] =='11': write_tape= 'b'
    if  elements[3] =='111': write_tape= 'c'
    move ="R" if elements[4] == "1" else "L"
    if start_state not in states: states.append(start_state)
    if finish_state not in states: states.append(finish_state)

    key_ = (start_state , read_tape)
    Value_ = (finish_state , write_tape , move)
    transitions[key_] = Value_

start_state = "1"
final_states = {max(states)}
    
tt= TuringMachine(tape =list("11011011"),
    blank_symbol ="1",
    initial_state = start_state,
    final_states = final_states,
    transition_function= transitions
)

t0=time.time()
while not tt.final() and time.time()<= t0+1:
    tt.step()

if tt.flag ==True: print('Accepted') 
else: print('Rejected')
print('110111011')
# print(tt.__dict__)
print(tt._TuringMachine__transition_function ,sep='\n')
# print(transitions)