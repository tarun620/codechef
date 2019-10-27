T=int(input())
for _ in range(T):
      n,k=map(int,input().split())
      A=list(map(int,input().split()))
      A=sorted(A)
      sum=0
      for i in range(k):
            sum+=A[i]
      j=0
      for i in A:
            if i<=sum:
                  j+=1
            else:
                  break
      A=A[:j]
        


