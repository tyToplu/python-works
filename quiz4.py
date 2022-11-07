import sys
inputs=sys.argv
inputs.pop(0)
file=open(inputs[0],"r")
the=file.readlines()
file.close()
the[-1]=the[-1]+"\n"
file=open(inputs[1],"w")
y=set()
the2=[]
for i in the:
	i=i.split("\t")
	the2.append(i)
for i in the2:
    y.add(i[0])
list1=[]
y=set()
for i in the2:  #bu kısım listedeki birinci değeri sözlüğün
    y.add(i[0])  #anahtar değeri yapıyor. Listedeki ikinci değeri 
y=tuple(y)    #ise o anahtar değerin karşılığı yapıyor
dic=dict()
for j in range(len(y)):
    dic[y[j]]=[]
for i in the2:
    for j in range(len(y)):
        if i[0]==y[j]:
            dic[y[j]].append(i)
dic2={}
for k,v in dic.items():  #bu kısım listedeki anahtar kelimeyi daha sonra sıralayabilmek içi
        dic2[int(k)]=v  #tamsayı haline getiriyor.
for i in dic2.keys():  #burada da sıralıyoruz
        list1.append(i)
        list1.sort()
list2=[]
for i in list1:
        dic3={}# her seferinde yeni sözlük oluşturuyoruz ki öncekinden eklediğimiz değerlerle karışmasın
        for j in dic2[i]:#Bu kısımda yeni bir sözlük oluşturuyoruz. Her ID'den gelen için ayrı bir sözlük
                dic3[int(j[1])]=j#Anahtar kelimeler gelen mesajların sıralaması oluyor.
        index=list1.index(i)#Sıranın başına mesaj 1 yazdırabilmek için indisi muhafaza ediyoruz.
        for k in dic3.keys():#Anahtar kelimeleri sırasıyla çağırabilmek için listeye attık. bu listeyi sıralayıp 
                list2.append(k)#bunu kullanarak değerleri çağıracağız
                list2.sort()
        file.write("message %d\n"%(index+1))
        for l in list2:
                file.writelines("\t".join(dic3[l]))#Burada da yazdırıyoruz artık.
        list2=[]
file.close()
                
        
        
                
        


      
                
        

        



            
        
        
            
            





