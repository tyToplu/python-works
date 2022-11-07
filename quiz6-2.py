import sys
number=int(sys.argv[1])
liste=[i*"*" for i in range(1,2*number,2)]
liste2=[i*"*" for i in range(2*number-1,0,-2)]
def printer(liste):
    global number
    for i in liste:
        print(i.center(2*number))
printer(liste)
printer(liste2[1:])