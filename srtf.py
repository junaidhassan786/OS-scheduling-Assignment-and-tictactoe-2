import Queue

q=Queue.Queue()

def findAvalibe(a=[],b=[],n=0,c=0):
    max=99999
    index=-1
    for i in range(0,n):
        if a[i]<=c:
            if b[i]>0 and b[i]<max:
                max=b[i]
                index=i
    if index != -1:
        q.put(index)    

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
        
        
    max=99999
    c_t=list(range(n))
    ct=0
    for i in range(0,n):
        c_t[i]=max

    findFirst(a_t,b_t,n)
    index=0
    index=q.get()
    if a_t[index] != 0:
        ct=ct+(a_t[index] - ct)
    b_t[index]-=1
    ct+=1
   
    findAvalibe(a_t,b_t,n,ct)
    while not(q.empty()):
        index=q.get()
        b_t[index]-=1
        ct+=1        
        if b_t[index]==0:
            c_t[index]=ct    
        findAvalibe(a_t,b_t,n,ct)            
    print "completion time"
    for i in range(0,n):
        print c_t[i]
    print "TAT"
    sum=0
    for i in range(0,n):
        tat[i]=c_t[i]-sat[i]
        print "P",i+1,tat[i]
        sum=sum+tat[i]
    avg=sum/n
    print "Avg TAT is : ",avg

main()