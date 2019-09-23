N,K,Q = [int(X) for X  in input().split()]
scores = [0 for i in range(N)]
for k in range(Q):
  q = int(input()) -1
  scores[q] +=1
  
for score in scores:
  if score >= Q - K + 1:
    print('Yes')
  else:
    print('No')

