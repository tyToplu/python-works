import sys
smn=sys.argv[1]
command=sys.argv[2]
def reader(filE,split_parameter):
    with open(filE,"r") as txt:
        metin=txt.readlines()
        for j in range(len(metin)):
            metin[j]=metin[j].strip('\n ')
        cmd2=[]
        for i in metin:
            i=i.split(split_parameter)
            cmd2.append(i)
    return cmd2
def printer():
    global i,set4,set5,file
    if i[2]=="2":
        if not set4==[]:
            file.writelines(["Suggestion List for ","'","%s"%i[1],"'" ," (when MD is 2):\n"])
            file.writelines(["'","%s"%i[1],"'"," has 2 mutual friends with ","'","%s"%"','".join(set4),"'",'\n'])
            if not set5==[]:
                file.writelines(["'",i[1],"'"," has 3 mutual friends with ","'","%s"%"','".join(set5),'\n'])
                file.writelines(["The suggested friends for ","'","%s"%i[1],"'",":","'","%s"%"','".join(set4)," %s"%",".join(set5),"'",'\n'])
            else:
                file.writelines(["The suggested friends for ","'","%s"%i[1],"'",":","'","%s"%"','".join(set4),"'",'\n'])


        else:
            print("He/She has no mutual friend when mutually degree is 2. Hence he/she has no suggested friends list.")
    if i[2]=="3":
            if not set5==[]:
                file.writelines(["Suggestion List for ","'","%s"%i[1],"'" ," (when MD is 3):",'\n'])
                file.writelines(["'","%s"%i[1],"'"," has 3 mutual friends with ","'","%s"%"','".join(set5),"'",'\n'])
                file.writelines(["The suggested friends for ","'","%s "%i[1],"'", ":","'","%s"%"','".join(set5),"'",'\n'])
            else:
                print("He/She has not mutual friend when mutually degree is 3")
commands=reader(command," ")
list_users2=reader(smn,":")
for i in list_users2:
        i[1]=i[1].split(' ')
        index=list_users2.index(i)
        list_users2[index][1]=i[1]
y=set()
for i in list_users2:
    y.add(i[0])
y=tuple(y)
dic=dict()
for i in list_users2:  #Anahtar kelime bir kişinin adı. Karşılığı ise liste içinde kişlerin adları
    for j in range(len(y)):
        if i[0]==y[j]:
            dic[y[j]]=i[1]
with open("output.txt","w") as file:
    for i in commands:
        if i[0] == "ANU":
            if i[1] in dic.keys():
                file.writelines("ERROR: Wrong input type! for \'ANU\'! -- This user already exists!!\n")
            else:
                dic[i[1]] = []
                file.writelines(["User ","'" ,"%s"%i[1],"'", " has been added to the social network successfully.\n"])
        elif i[0] == "DEU":
            if i[1] in dic.keys():
                dic.pop(i[1])
                for k, v in dic.items():
                    if i[1] in v:
                        v.remove(i[1])
                        dic[k] = v
                file.writelines(["User ","'", "%s"%i[1],"'", " and his/her all relations have been deleted successfully.\n"])
            else:
                file.writelines(["ERROR: Wrong input type! for \'DEU\'!--There is no user named ","'","%s"%i[1],"'", "!!","\n"])
        elif i[0] == "ANF":
            if i[1] not in dic.keys() and i[2] not in dic.keys():
                file.writelines(["ERROR: Wrong input type! for \'ANF\'! -- No user named ", "'","%s"%i[1],"'", " and ","'", "%s"%i[2],"'", " found!\n"])
            elif i[1] in dic.keys() and i[2] not in dic.keys():
                file.writelines(["ERROR: Wrong input type! for \'ANF\'! -- No user named ", "'","%s"%i[2],"'", " found!!\n"])
            elif i[1] not in dic.keys() and i[2] in dic.keys():
                file.writelines(["ERROR: Wrong input type! for \'ANF\'! -- No user named ", "'","%s"%i[1],"'", " found!!\n"])
            elif i[1] in dic.keys() and i[2] in dic.keys():
                if i[2] not in dic[i[1]]:
                    store_friends = dic[i[1]]
                    store_friends.append(i[2])
                    dic[i[1]] = store_friends
                    store_friends2 = dic[i[2]]
                    store_friends2.append(i[1])
                    dic[i[2]] = store_friends2
                    file.writelines(["Relation between ", "'","%s"%i[1],"'", " and ", "'","%s"%i[2],"'", " has been added successfully\n"])

                else:
                    file.writelines(["ERROR: A relation between ", "'","%s"%i[1],"'", " and ","'","%s"%i[2],"'", " already exists!!\n"])
        elif i[0] == "DEF":
            if i[1] not in dic.keys() and i[2] not in dic.keys():
                file.writelines(["ERROR: Wrong input type! for \'DEF\'! -- No user named ", "'","%s"%i[1],"'", " and ", "'","%s"%i[2],"'", " found!\n"])
            elif i[1] in dic.keys() and i[2] not in dic.keys():
                file.writelines(["ERROR: Wrong input type! for \'DEF\'! -- No user named ", "'","%s"%i[2],"'", " found!!\n"])
            elif i[1] not in dic.keys() and i[2] in dic.keys():
                file.writelines(["ERROR: Wrong input type! for \'DEF\'! -- No user named ", "'",i[1],"'", " found!!\n"])
            elif i[1] in dic.keys() and i[2] in dic.keys():
                if i[2] in dic[i[1]]:
                    store_friends4 = dic[i[1]]
                    store_friends4.remove(i[2])
                    dic[i[1]] = store_friends4
                    store_friends3 = dic[i[2]]
                    store_friends3.remove(i[1])
                    dic[i[2]] = store_friends3
                    file.writelines(["Relation between ","'","%s"%i[1],"'", " and ", "'","%s"%i[2],"'", " has been deleted successfully\n"])
                else:
                    file.writelines(["ERROR: No relation between ","%s"%i[1], " and ", "%s"%i[2], " found!!\n"])
        elif i[0] == "CF":
            if i[1] not in dic.keys():
                file.writelines(["ERROR: Wrong input type! for '\CF\'! -- No user named ", "%s"%i[1], " found!\n"])
            else:
                file.writelines(["User ", "%s"%i[1], " has ", "%s"%len(dic[i[1]]), " friends\n"])
        elif i[0] == "FPF":
            if i[1] not in dic.keys():
                file.writelines(["ERROR: Wrong input type! for 'FPF'! -- No user named ", "%s"%i[1], " found!\n"])
            else:
                set1 = set()
                if int(i[2]) == 1 or int(i[2]) == 2 or int(i[2]) == 3:
                    set1 = set(dic[i[1]])
                    list0 = list(set1)
                    list0.sort()
                    if not (int(i[2]) == 2) and not (int(i[2]) == 3):
                        file.writelines(["User ", ",", "%s"%i[1], "'", " have ", "%s"%len(set1)," possible friends when maximum distance is 1","\n","These are the possible friends: ","{","'" ,"%s"%"','".join(list0),"'","}",'\n'])
                if int(i[2]) == 2 or int(i[2]) == 3:
                    set2 = set()
                    for j in set1:
                        for k in dic[j]:
                            set2.add(k)
                    set2 = set1 | set2
                    if i[1] in set2:
                        set2.remove(i[1])
                    list1 = list(set2)
                    list1.sort()
                    if not int(i[2]) == 3:
                        file.writelines(["User ", "'", "%s"%i[1], "'", " have ", "%s"%len(set2)," possible friends when maximum distance is 2\n","These are the possible friends: ","{","'" ,"%s"%"','".join(list1),"'","}",'\n',])
                if int(i[2]) == 3:
                    set3 = set()
                    for l in set2:

                        for m in dic[l]:
                            set3.add(m)
                    set3 = set3 | set2
                    if i[1] in set3:
                        set3.remove(i[1])
                    list2 = list(set3)
                    list2.sort()
                    file.writelines(["User ", "'", "%s"%i[1], "' ", "have ", "%s"%len(set3)," possible friends when maximum distance is 3\n", "These are possible friends: ","{", "'","%s"%"','".join(list2),"'","}",'\n'])
                if int(i[2]) not in [1, 2, 3]:
                    file.writelines(["Out of range.Wrong input for FPF\n"])
        if i[0] == "SF":
            if i[1] not in dic.keys():
                file.writelines(["Error: Wrong input type! for \'SF\'! -- No user named ", "%s"%i[1], " found!!","\n"])
            elif int(i[2]) > 3 or int(i[2]) < 2:
                file.writelines(["Error: Mutually Degree cannot be less than 1 or greater than 4\n"])
            else:
                if int(i[2]) == 2 or int(i[2]) == 3:
                    dic2 = {2: [], 3: []}
                    for k, v in dic.items():
                        count = 0
                        for u in dic[i[1]]:
                            if u in v:
                                count += 1
                        if count == 2:
                            dic2[2].append(k)
                        if count == 3:
                            dic2[3].append(k)
                    set4, set5 = set(dic2[2]), set(dic2[3])
                    set4, set5 = set4 - set(dic[i[1]]), set5 - set(dic[i[1]])
                    set5.discard(i[1])
                    set4.discard(i[1])
                    set4, set5 = sorted(list(set4)), sorted(list(set5))
                printer()
