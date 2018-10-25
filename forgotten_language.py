t=input()
for i in range(t):
    n,k=map(int,raw_input().split())
    L1=list(map(str,raw_input().split()))
    L2,L3=[],[]
    s=''
    for i in range(k):
        L2=list(map(str,raw_input().split()))
        L2.pop(0)
        L3.append(L2)
    for i in L1:
        cnt=0
        for j in L3:
            for k in j:
                if i==k:
                    cnt+=1
        if cnt==0:
            s+='NO '
        else:
            s+='YES '
    s=s[:len(s)]
    print s        
