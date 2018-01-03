def turn(arr=[],n=5):
    max=99999
    for i in range(0,n):
       if arr[i]<max:
           index=i
           max=arr[i]
    max=99999
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
    
    ct=0
    c_t=list(range(n));
    for i in range(0,n):
        if i>0:
            pre=x;
        x=turn(a_t,n)
        if i==0 and a_t[x]!=0:
            ct=ct+a_t[x];

        if (i>0 and (a_t[x]-c_t[pre])>0):
            y=a_t[x]-c_t[pre]
            ct=ct+b_t[x]+y
        else:
            ct=ct+b_t[x]
        c_t[x]=ct
        a_t[x]=max
    print "completion time"
    for i in range(0,n):
        print "P",i+1,c_t[i]

    sum=0
    print "TAT"
    for i in range(0,n):
        tat[i]=c_t[i]-sat[i]
        print "P",i+1,tat[i]
        sum=sum+tat[i]
    avg=sum/n
    print "Avg TAT is : ",avg


main()                