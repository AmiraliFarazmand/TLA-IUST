results=[]
# FA formation in dictionary:{state_name : [[transition rule ,destination state] , is_final ]} 
states={}
states_line =list( input().replace('{','').replace('}','').replace(' ','').split(','))
alphabet_line =list( input().replace('{','').replace('}','').replace(' ','').split(','))
finals_line =list( input().replace('{','').replace('}','').replace(' ','').split(','))
current_state = states_line[0]
for st in states_line:                                              #states
    if st in finals_line:
        state = {st:[[] , 1]} #1 for final states
    else:
        state = {st:[[] , 0]} #0 for non-final states
    states.update(state)
for i in range(int(input())):                                       #transition rule
    ls = list( input().replace(' ','').split(','))
    des= [ls[1], ls[2]]
    states[ls[0]] [0].append(des)

w=input()
pointer=0
flag =0

def check_done(current,input_list , pointer):
  if pointer < len(input_list):
    for i in range(len(states[current][0])):
        if states[current][0][i][0] == input_list[pointer]:
            check_done(states[current][0][i][1],input_list,pointer+1)
            # print(f'l28:check_done({states[current][0][i][1]},{input_list},{pointer+1})')

        if states[current][0][i][0]== '$':
            check_done(states[current][0][i][1],input_list,pointer)
            # print(f'l32:check_done({states[current][0][i][1]},{input_list},{pointer})')

        if states[states[current][0][i][1]][1]==1 and pointer==len(input_list)-1 and states[current][0][i][0] == input_list[pointer]:
            results.append('1')
            # print('l36:done, pointer',pointer,input_list[pointer],'//des:' ,states[current][0][i][1],' : ',states[states[current][0][i][1]] )
            # print('Accepted')
            # exit(0)
        else:
            results.append('0')


check_done(current_state,w,pointer)
print ('Accepted')if '1' in results else print("Rejected")

