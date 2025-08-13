reviews =input("Enter records separated by semicolon:\n").split(';')
records,L=[],[]
def store_all_records(reviews):
    i=0
    while i<len(reviews):
        d={}
        d['Name']=reviews[i].split(',')[0]
        d['Department']=reviews[i].split(',')[1]
        d['Score']=reviews[i].split(',')[2]
        records.append(d)
        i+=1
store_all_records(reviews)
def display_all(records):
    for i,char in enumerate(records):
        print("Record",i+1,":",char)
def record_by_index(records,i):
    if i-1<len(records):
        print("Needed record:",records[i-1])
    else:
        print("Record not found")
def display_toppers(records):
    L.clear()
    R=list(filter(lambda x:int(x['Score'])>80,records))
    P=sorted(R,key=lambda x:int(x['Score']))
    L.extend(list(map(lambda x:x['Name'],P)))
    return L
def display_by_dept(records,dept):
    R=list(filter(lambda x:x['Department']==dept,records))
    if R==[]:
        print("Department not found")
    else:
        return R
def top_in_dept(records,dept):
    R=list(filter(lambda x:x['Department']==dept,records))
    if R==[]:
        print("Department not found")
    else:
        P=sorted(R,key=lambda x:int(x['Score']))
        return P[0]['Name']
def top_each_dept(records):
    R=list(set(map(lambda x:x['Department'],records)))
    for char in R:
        P=top_in_dept(records,char)
        print("Topper in ",char,":",P)
def error():
    try:
        i=int(input("Enter a choice:"))
        return i
    except Exception:
        print("INVALID!!,Enter valid choice")
        return error()
print("1. Display all records")
print("2. Display one record by index")
print("3. Display all top performers (score > 80)")
print("4. Display records by department")
print("5. Display top performer in a given department")
print("6. Display top performer in every department")
print("7.Exit")
while True:
    s=error()
    if s==1:
        display_all(records)
    elif s==2:
        i=int(input("Enter needed record numner:"))
        record_by_index(records,i)
    elif s==3:
        a= display_toppers(records)
        if a==[]:
            print("There are no toppers")
        else:
            print("The toppers are:",a)
    elif s==4:
        dept=input("Enter department name:")
        a=display_by_dept(records,dept)
        print("Records of",dept,":",a)
    elif s==5:
        dept=input("Enter department name:")
        a=top_in_dept(records,dept)
        print("Topper in",dept,":",a)
    elif s==6:
        top_each_dept(records)
    elif s==7:
        break
    else:
        print("Choice not availabe,Try again")
    

