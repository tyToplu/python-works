import sys
inputs=sys.argv
inputs.pop(0)
output=[]
def lister():
    output.append(inputs)
    inp=int(inputs[0])**int(inputs[1])
    output.append(inp)
    while inp>9 :
        inp=str(inp)
        inp=[i for i in inp]
        output.append(inp)
        total=0
        for i in inp:
            i=int(i)
            total+=i
        inp=total
        output.append(inp)
lister()
x=''
x+=output[0][0]+'^'+output[0][1]+' = '
for i in output[1:]:
    if type(i)==type([]):
        for j in i:
            x+=str(j)+' + '
        x=x.strip(' +')
        x+=' = '
    elif type(i)==type(5):
        x+=str(i)+' = '
x=x.strip('= ')

print(x)
        
        



    
    
