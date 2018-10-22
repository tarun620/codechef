t=input()
for i in range(t):
    n,k=map(int,raw_input().split())
    L1,L2=[],[]
    for i in range(n):
        T,D=map(int,raw_input().split())
        L1.append(T)
        L2.append(D)
    s,s1,c=0,0,0
    while k>0:
        if L1[0]<=k:
            k-=L1[0]
            L1.remove(L1[0])
            c+=1
        else:
            L1[0]-=k
            break
    for i in range(c):
        L2.remove(L2[0])
    for i in range(len(L1)):
        s1+=L1[i]*L2[i]
    print s1
                
        
            
        
    
