n=list(input())

a=[]

for j in range(len(n),0,-1):
 
   for i in range(0,len(n)):

        b=n[i:j]

        if len(set(b))>0:

            a.append(len(set(b)))

print(max(a))