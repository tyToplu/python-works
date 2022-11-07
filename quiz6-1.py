import sys
number=int(sys.argv[1])
count=0
start=number-1
end=number
liste=[" "]*(number*2-1)
def printer(sayı,start1,end1,liste):
    global count
    if count<sayı:
        count+=1
        liste[start1:end1]="*"*(end1-start1)
        print("".join(liste))
        printer(sayı,start1-1,end1+1,liste)
def reverse_printer(sayı,start1,end1,liste):
    global count
    if count>=1:
        count-=1
        liste[start1]=" "
        liste[end1]=" "
        print("".join(liste))
        reverse_printer(sayı,start1+1,end1-1,liste)
printer(number,start,end,liste)
reverse_printer(number,0,len(liste)-1,liste)