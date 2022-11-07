import sys
inputs=sys.argv
inputs.pop(0)
inputs=inputs[0]
inputs=inputs.split(',')
for i in inputs:
    if int(i) < 0:
        inputs.remove(i)
    for i in range(len(inputs)):
        inputs[i]=int(inputs[i])

inputs.sort()
    
if inputs[0]==1:
    for i in inputs:
        if int(i) < 0:
            inputs.remove(i)
    for i in range(len(inputs)):
        inputs[i]=int(inputs[i])
    
    inputs.sort()
    for i in range(1,len(inputs),2):
        inputs[i]=''
    for i in range(inputs.count('')):
        inputs.remove('')

    l=inputs[1:]

    k=len(inputs)
    a=1
    def the():
        global a    
        y=inputs[a]
        for i in range(y-1,k,y):
            if i==1:
                continue
            if len(inputs)<i:
                break
            inputs[i]=''
        z=inputs.count('')
        for i in range(z):
            inputs.remove('')
        if a<len(inputs)-1:
            a+=1
            the()
    the()
    print(*inputs)

else:
    k=len(inputs)
    a=0
    def the():
        global a    
        y=inputs[a]
        for i in range(y-1,k,y):
            if len(inputs)<i:
                break
            inputs[i]=''
        z=inputs.count('')
        for i in range(z):
            inputs.remove('')
        if a<len(inputs)-1:
            a+=1
            the()
    the()
    print(*inputs)
    

    
    
    

    
    

