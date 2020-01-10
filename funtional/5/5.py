from main import n
l=[]
p=[]
for i in range(1,n):
    if(n%i==0):
        l.append(i)
for i in l:
    if(i%2!=0):
        p.append(i)
print("the primefactors of {} are".format(n))
print(p)
