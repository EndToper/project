arr = {}
###### РУССКИЕ БУКВЫ
for i in range(1040,1106):
    arr[chr(i)] = []
    for elem in list(f'{i:b}'.rjust(12, '0')):
        arr[chr(i)].append(int(elem))


# ###### АНГЛИЙСКИЕ БУКВЫ
for i in range(33,127):
    arr[chr(i)] = []

    for elem in list(f'{i:b}'.rjust(12, '0')):
        arr[chr(i)].append(int(elem))
arr[' '] = [1,1,1,1,1,1,1,1,1,1,1,1]
arr['■'] = [1,0,0,0,0,0,0,0,0,0,0,1]
y = ord('\n')
arr['\n'] = []
for elem in list(f'{y:b}'.rjust(12, '0')):
    arr['\n'].append(int(elem))





dearr = {}
###### РУССКИЕ БУКВЫ
for i in range(1040,1106):
    key = ''
    for elem in list(f'{i:b}'.rjust(12, '0')):
        key += elem
    dearr[key]=chr(i)



# ###### АНГЛИЙСКИЕ БУКВЫ
for i in range(33,127):
    key = ''
    for elem in list(f'{i:b}'.rjust(12, '0')):
        key += elem
    dearr[key] = chr(i)

dearr['111111111111'] = ' '
dearr['100000000001'] = '■'
dearr['000000001010']='\n'

