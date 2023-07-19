'''getting inputs'''
states={}
states_line =list( input().replace('{','').replace('}','').replace(' ','').split(','))
alphabets =list( input().replace('{','').replace('}','').replace(' ','').split(','))
final_states =list( input().replace('{','').replace('}','').replace(' ','').split(','))
current_state = states_line[0]
tr_num = int(input())
'''making states in FA form'''
# FA formation in dictionary:{state_name : [[transition rule ,destination state] , is_final ]} 
for st in states_line:          #states
    if st in final_states:
        state = {st:[[] , 1]} #1 for final states
    else:
        state = {st:[[] , 0]} #0 for non-final states
    states.update(state)
transition_rules=[]
for i in range(tr_num):       #transition rule
    ls = list( input().replace(' ','').split(','))
    des= [ls[1], ls[2]]
    states[ls[0]] [0].append(des)
    transition_rules.append(des)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''                                               FUNCTIONS:                                                     '''
'''REPLACE FUNCTION'''
def replace (target ,r_with):
    for i in states :
        for j in range(len(states[i][0])):
            # print(states[i][0][j][1])
            if states[i][0][j][1]==target: # replace destenitions
                # print(states[i][0][j],'@@@@@@@@@@')
                states[i][0][j][1]=str(r_with)
        
    del states [target]

'''REACHABLE FUNCTION'''
reachable_states=[current_state]
unreachable_states=[]
def reachable(states,current_state):
    for st in (states[current_state][0]):
        if st[1] not in reachable_states :
            reachable_states.append(st[1]) 
            current_state= st[1]
            reachable(states ,current_state)

'''SAME_STATES FUNCTION'''
def same_states():
    for st1 in states:
        for st2 in states:
            # print(st1 , st2) if st1 != st2 else ("")
            if st1 != st2:
                tr1= sorted(states[st1][0])
                tr2= sorted(states[st2][0])
                # print(tr1,'******', tr2)
                if tr1 == tr2 and states[st1][1] == states[st2][1]: #same outputs and same position based on being final and non-final states
                    # print(f'{st2} replaced with {st1}')
                    replace(st2 ,st1)
                    same_states()
                    return 
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''        
# removing unreachable states from states dict:
reachable(states , current_state)
for st in states :
    if st not in reachable_states:
        unreachable_states.append(st)
for i in unreachable_states:
    states.pop(i) 

# removing same states:
same_states()
print(len(states))