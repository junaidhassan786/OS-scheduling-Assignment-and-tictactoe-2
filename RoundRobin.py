import Queue

q=Queue.Queue()
temp=Queue.Queue()

def findNext(a=[],b=[],n=0,c=0):
    bl=True
    for i in range(0,n):
        if a[i]<=c:
            if b[i]!=0:            
                while not(q.empty()):
                    index=q.get()
                    if index==i:
                        bl=False
                    else:
                        bl=True
                    temp.put(index)
                while not(temp.empty()):
                    index=temp.get()
                    q.put(index)

                if bl:
                    q.put(i)

def findFirst(a=[],b=[],n=0):
    index=0
    max=99999
    for i in range(0,n):
        if a[i]<max:
            max=a[i]
            index=i
    q.put(index)

def main():
    print "Enter number of process : ",
    n=input()
    
    b_t=list(range(n))
    print "Enter burst time for process "
    for i in range(0,n):
        print "P",i+1," : ",
        b_t[i]=input()
    
    a_t=list(range(n))
    print "Enter arrival time for process"
    for i in range(0,n):
        print "P",i+1," : ",
        a_t[i]=input()
        
    sat=list(range(n))
    for i in range(0,n):
        sat[i]=a_t[i]
    
    tat=list(range(n))        
        
    print "Enter quantum time for process : ",
    qt=input()
    
    ct=0
    c_t=list(range(n))

    findFirst(a_t,b_t,n)
    index=0
    index=q.get()
    if a_t[index] != 0:
        ct=ct+a_t[index]
    if b_t[index]>=qt:
        b_t[index]-=qt
        ct+=qt
    else:
        ct+=b_t[index]
        b_t[index]=0
    findNext(a_t,b_t,n,ct)
    if b_t[index]!=0:
        q.put(index)
    else:
        c_t[index]=ct   
    while not(q.empty()):
        index=q.get()
        if b_t[index]>=qt:
            b_t[index]-=qt
            ct+=qt
        else:
            ct+=b_t[index]
            b_t[index]=0
        findNext(a_t,b_t,n,ct)
        if b_t[index]!=0:
            q.put(index)
        else:
            c_t[index]=ct
    print "completion time"
    for i in range(0,n):
        print c_t[i]            
    sum=0
    print "TAT"
    for i in range(0,n):
        tat[i]=c_t[i]-sat[i]
        print "P",i+1,tat[i]
        sum=sum+tat[i]
    avg=sum/n
    print "Avg TAT is : ",avg
               
main()