print('<-----RULES----->','1. BRUSH DOWN','2. BRUSH UP','3. VEHİCLE ROTATES RİGHT','4. VEHİCLE ROTATES LEFT','5. MOVE UP TO X','6. JUMP','7. REVERSE DİRECTİON','8. VİEW THE MATRIX','0. EXİT',sep='\n')
inputs=input('please enter the commands with a plus(+) sign between them.\n')
inputs=inputs.split('+')
response='no'
x=1
y=1
z=[]
number=0
i=[1,2,3,4,5]
def right():
    global değiş
    global x
    global y
    for j in range(değiş):
        if y==len(z)-2:
            y=1
            if response=='yes':
                brush_down()
        else:
            y+=1
            if response=='yes':
                brush_down()
def down():
    global değiş
    global x
    global y
    for j in range(değiş):
        if x==len(z)-2:
            x=1
            if response=='yes':
                brush_down()
        else:
            x+=1
            if response=='yes':
                brush_down()
def left():
    global değiş
    global x
    global y
    for j in range(değiş):
        if y==1:
            y=len(z)-2
            if response=='yes':
                brush_down()
        else:
            y-=1
            if response=='yes':
                brush_down()
def up():
    global değiş
    global x
    global y
    for j in range(değiş):
        if x==1:
            x=len(z)-2
            if response=='yes':
                brush_down()
        else:
            x-=1
            if response=='yes':
                brush_down()
def right_j():
    global x
    global y
    global response
    if y==len(z)-2:
        y=3
        
    elif y+3>len(z)-2:
        y=y+3-len(z)+2
    else:
        y+=3
    response='no'
def left_j():
    global x
    global y
    global response
    if y==1:
        y=len(z)-2-3
    elif y-3<1:
        y=y-3+len(z)-2
    else:
        y-=3
    response='no'
def up_j():
    global x
    global y
    global response
    if x==1:
        x=len(z)-2-3
    elif x-3<1:
        x=len(z)-2+x-3
    else:
        x-=3
    response='no'
def down_j():
    global x
    global y
    global response
    if x==len(z)-2:
        x=1+3
    elif x+3>len(z)-2:
        x=x+3-len(z)+2
    else:
        x+=3
    response='no'
direction=[right,down,left,up]
direction_j=[right_j,down_j,left_j,up_j]
def n_size(N):
    for i in range(N):
        z.insert(0,['+','+'])
    z.insert(0,(N+2)*['+'])
    z.insert(len(z),(N+2)*['+'])
    for i in range(N):
        for i in range(1,N+1):
            z[i].insert(1,' ')
    return z
def brush_down():
    global response
    if response=='yes':
        z[x][y]='*'
    elif response=='no':
        pass
testi=[]    
n_size(int(inputs[0]))
testi=list(map(lambda x:'5_'+str(x),[i for i in range(500)]))
testi+=['0','1','2','3','4','6','7','8']
def esas_işlem():
    global response,inputs,değiş,number,x,y,z,i,testi
    aresp=False
    while aresp==False:
        for i in inputs[1:]:
            if i in testi:
                continue
            else:
                inputs=input('you entered an incorrect command, please try again!\n')
                inputs=inputs.split('+')
                break
        aresp=True
    for i in inputs[1:]:
        if '_' and '5' in i:
            i=i.split('_')
            değiş=int(i[1])
            direction[number]()
        elif i=='1':
            response='yes'
            brush_down()
        elif i=='2':
            response='no'
        elif i=='3':  #right
            if number>=3:
                number=0
            else:
                number+=1
        elif i=='4':  #left
            if number<=0:
                number=3
            else:
                number-=1
        elif i=='6':
            direction_j[number]()
        elif i=='7':
            number+=2
            if number>3:
                number-=4
        elif i=='8':
            for i in range(int(inputs[0])+2):
                for j in range(int(inputs[0])+2):
                    print(z[i][j],end="")
                print()
        elif i=='0':
            break
#error handling       
esas_işlem()

