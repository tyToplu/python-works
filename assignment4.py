import sys
with open(sys.argv[1],"r") as f:
    readed=f.readlines()
matrix=[]
def reader():
    global readed,readed2
    for i in readed:
        i.split("\n ") #sonuna başına yanlışlıkla bir boşluk koymuşsa onu da almayalım diye.
        matrix.append(i.split())
reader()
def printer():
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()
x,y=0,0
def right_seeker(x,y):
    """store input olarak verilen değeri tutan bir değişken. burada yaptığım
    matrix'te gitmek istenen yönde değeri bir artırıp kontrol etmekten ibaret
    her while döngüsünün altında tekrar kontrol ediyorum sağda,solda,yukarıda
    aşağıda bu store değerine eşit bir değer var mı diye en son a'yı istenen
    yöne gidecek şekilde güncelleyip devam ediyorum.en son while'den çıkıp
    ilk başladığımız yerin sağında solunda bir şey var mı diye kontrol ediyoruz
    """
    global count
    try:
        a=x+1
        type(matrix[y][a])==str
    except Exception:
        left_seeker(x,y)#bu noktaya dikkat et
        return
    while matrix[y][a]==store:
        if a==x+1:
            pass
        matrix[y][a]=" "
        count += 1
        try:
            if a-1==-1:
                pass
            elif matrix[y][a - 1] == store:
                left_seeker(a, y)
        except:
            pass
        try:
            if y-1==-1:
                pass
            elif matrix[y - 1][a] == store:
                up_seeker(a,y)
        except:
            pass
        try:
            if matrix[y + 1][a] == store:
                down_seeker(a,y)
        except:
            pass
        try:
            if matrix[y][a + 1] == store:
                a += 1
        except:
            break
    try:
        if x-1==-1:
            pass
        elif matrix[y][x-1]==store:
            left_seeker(x,y)
    except:
        pass
    try:
        if y-1==-1:
            pass
        elif matrix[y-1][x]==store:
            up_seeker(x,y)
    except:
        pass
    try:
        if matrix[y+1][x]==store:
            down_seeker(x,y)
    except:
        pass
    return a, y
def left_seeker(x,y):
    global count
    try:
        if x-1==-1:
            right_seeker(x,y)
            return
        else:
            a=x-1
        assert type(matrix[y][a])==str
    except Exception:
        return
    while matrix[y][a]==store:
        if a==x-1:
            pass
        matrix[y][a]=" "
        count += 1
        try:
            if matrix[y][a + 1] == store:
                right_seeker(a,y)
        except:
            pass
        try:
            if y-1==-1:
                pass
            elif matrix[y - 1][a] == store:
                up_seeker(a,y)
        except:
            pass
        try:
            if matrix[y + 1][a] == store:
                down_seeker(a,y)
        except:
            pass
        try:
            if a-1==-1:
                pass
            elif matrix[y][a-1]==store:
                a-=1
        except:
            break
    try:
        if matrix[y][x+1]==store:
            right_seeker(x,y)
    except:
        pass
    try:
        if y-1==-1:
            pass
        elif matrix[y-1][x]==store:
            up_seeker(x,y)
    except:
        pass
    try:
        if matrix[y+1][x]==store:
            down_seeker(x,y)
    except:
        pass
    return a, y
def up_seeker(x,y):
    global count
    try:
        if y-1 == -1:
            down_seeker(x,y)
            return
        else:
            a=y-1
        assert type(matrix[a][x])==str
    except Exception:
        return
    while matrix[a][x]==store:
        if a==y-1:
            pass
        matrix[a][x]=" "
        count += 1
        try:
            if x-1==-1:
                pass
            elif matrix[a][x - 1] == store:
                left_seeker(x,a)
        except:
            pass
        try:
            if matrix[a][x+1] == store:
                right_seeker(x,a)
        except:
            pass
        try:
            if matrix[a + 1][x] == store:
                down_seeker(x,a)
        except:
            pass
        try:
            if a-1==-1:
                pass
            elif store == matrix[a - 1][x]:
                a-=1
        except:
            break
    try:
        if x-1==-1:
            pass
        elif matrix[y][x-1]==store:
            left_seeker(x,a)
    except:
        pass
    try:
        if y-1==-1:
            pass
        elif matrix[y-1][x]==store:
            up_seeker(x,y)
    except:
        pass
    try:
        if matrix[y+1][x]==store:
            down_seeker(x,y)
    except:
        pass
    return x,a
def down_seeker(x,y):
    global count
    try:
        a=y+1
        type(matrix[a][x])==str
    except:
        return
    while matrix[a][x]==store:
        if a==y+1:
            pass
        matrix[a][x]=" "
        count+=1
        try:
            if x-1==-1:
                pass
            elif matrix[a][x - 1] == store:
                left_seeker(x,a)
        except:
            pass
        try:
            if a-1==-1:
                pass
            elif matrix[a - 1][x] == store:
                up_seeker(x,a)
        except:
            pass
        try:
            if matrix[a][x+1] == store:
                right_seeker(x,a)
        except:
            pass
        try:
            if matrix[a+1][x]==store:
                a+=1
        except:
            break
    try:
        if x-1==-1:
            pass
        elif matrix[y][x-1]==store:
            left_seeker(x,y)
    except:
        pass
    try:
        if y-1 ==-1:
            pass
        if matrix[y,-1][x]==store:
            up_seeker(x,y)
    except:
        pass
    try:
        if matrix[y][x+1]==store:
            right_seeker(x,y)
    except:
        pass
    return x,a

def bomber(x,y):
    global score, dic,matrix,count_for_bomb
    count_for_bomb=1
    for i in range(len(matrix)):
        try:
            if matrix[i][x]=="X" and not i==y:
                bomber(x,i)
            elif not matrix[i][x]==" ":
                score+=dic[matrix[i][x]]
                matrix[i].pop(x)
                matrix[i].insert(x," ")
        except:
            pass
    for j in range(len(matrix[0])):
        try:
            if matrix[y][j]=="X"and not j==x:
                bomber(j,y)
            elif not matrix[y][j]==" ":
                score+=dic[matrix[y][j]]
                matrix[y].pop(j)
                matrix[y].insert(j," ")
        except:
            pass
def if_ended():
    global check
    for y1 in range(len(matrix)):
        for x1 in range(len(matrix[y1])):
            try:
                if y1-1==-1:
                    pass
                elif matrix[y1][x1]==matrix[y1-1][x1]  and matrix[y1][x1]!=" ":
                    return True
            except:
                    pass
            try:
                if matrix[y1][x1]==matrix[y1+1][x1]and matrix[y1][x1]!=" ":
                    return True
            except:
                pass
            try:
                if x1-1==-1:
                    pass
                elif matrix[y1][x1-1]==matrix[y1][x1]and matrix[y1][x1]!=" ":
                    return True
            except:
                pass
            try:
                if  matrix[y1][x1]==matrix[y1][x1+1]and matrix[y1][x1]!=" ":
                    return True
            except:
                pass
            try:
                if matrix[y1][x1]=="X":
                    return True
            except:
                pass
            else:
                continue
    printer()
    print("\nYour score is: ",score_calculator())
    print("Game over!")
    check=False
def is_space():
    global matrix
    try:
        for i in range(len(matrix)):
            if matrix[i]==[" "]*len(matrix[0]):
                matrix.pop(i)
    except:
        pass
def is_space_vertical():
    global matrix
    transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    try:
        for k in range(len(transpose)):
            if transpose[k]==[" "]*len(transpose[0]):
                transpose.pop(k)
    except:
        pass
    matrix = [[row[i] for row in transpose] for i in range(len(transpose[0]))]

def list_slider():
    global matrix
    transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    def blank_carrier(liste):
        global matrix
        for i in range(len(liste)):
            count = 0
            count = liste[i].count(" ")
            for k in range(count):
                liste[i].remove(" ")
            for k in range(count):
                liste[i].insert(0, " ")
        return liste
    blank_carrier(transpose)
    matrix=[[row[i] for row in transpose] for i in range(len(transpose[0]))]
def input_converter():
    global y,x,count
    print("Your score is: ",score_calculator())
    inputs = input("Please enter a row and a column: ")
    count=0
    inputs = inputs.split(" ")
    inputs = [b.strip(" ") for b in inputs]
    y, x = int(inputs[0]), int(inputs[1])
    try:
        assert type(matrix[y][x]) == type(" ")
    except Exception:
        print("Please enter a valid size!")
        input_converter()
    if matrix[y][x]== " ":
        print("Please enter a valid size!")
        input_converter()
def score_calculator():
    global count,score,dic
    dic={"B":9,"G":8,"W":7,"Y":6,"R":5,"P":4,"O":3,"D":2,"F":1,"X":0}
    if not count==0:
        score+=count*dic[store]
    return score
check=True
first_time,count_for_bomb,a,score,count,store=0,0,0,0,0,"A"
while check==True:
    printer()
    input_converter()
    store=matrix[y][x]
    if store=="X":
        bomber(x,y)
    else:
        right_seeker(x,y)
        down_seeker(x,y)
        left_seeker(x,y)
        up_seeker(x,y)
    list_slider()
    for i in range(5):#checks if there is any space
        is_space()
        try:
            is_space_vertical()
        except:
            pass
    first_time=1
    if_ended()




