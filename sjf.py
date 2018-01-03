import Queue
q=Queue.Queue()
def findAvalibe(a=[],b=[],n=0,c=0):
    max=99999
    for i in range(0,n):
        if a[i]<=c:
            q.put(i)
    sv=findSmallest(q,b)
    max=99999
    return sv
        
def findSmallest(q,b=[]):
    index=0
    max=99999
    while not(q.empty()):
        temp=q.get()
        if b[temp]<max:
            max=b[temp]
            index=temp
    return index 

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
        if a_t[i]<max:
            max=a_t[i]
            index=i
    
    max=99999
    if a_t[index]!=0:
        ct=ct+a_t[index]
    
    ct+=b_t[index]
    c_t[index]=ct
    a_t[index]=max
    b_t[index]=max

    for i in range(1,n):
        temp=findAvalibe(a_t,b_t,n,ct)
        ct+=b_t[temp]
        c_t[temp]=ct
        a_t[temp]=max
        b_t[temp]=max
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