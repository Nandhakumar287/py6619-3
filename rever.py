s,num = map (str,input().split())
n=int(num)
l=len(s)
a=s
for i in range(0,n):
    a=a[-1]+a[:l-1]
print(a)    
