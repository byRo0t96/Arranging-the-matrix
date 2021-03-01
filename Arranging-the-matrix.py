# usage:
# sort(list_1,'>') # < OR >

def sort(list_name,updown):
    op={'<':lambda x,y:x<y,'>':lambda x,y:x>y}
    sort=['']*len(list_name)
    sort_temp1=[]
    for i in range(len(list_name)):
        sort_temp2=[]
        for j in range(len(list_name)):
            if i!=j:
                if op[updown](list_name[i],list_name[j]):
                    sort_temp2.append(1)
                elif list_name[i]==list_name[j]:
                    sort_temp2.append(0)
                else:
                    sort_temp2.append(0)       
        sort_temp1.append(sort_temp2)
    for i in range(len(sort_temp1)):
        level=0
        for j in range(len(sort_temp1[i])):
            level=level+sort_temp1[i][j]
        if list_name.count(list_name[i])>1:
            for s in range(list_name.count(list_name[i])):
                sort[level+s]=list_name[i]
        else:
            sort[level]=list_name[i]
    return sort
