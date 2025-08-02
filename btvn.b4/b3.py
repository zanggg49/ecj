m,n=map(int,input().split())
arr=list(map(int,input().split()))
a=set(map(int,input("các số bạn thích").split()))
b=set(map(int,input("các số bạn không thích").split()))
h=0
for i in arr:
    if i in a: h+=1
    elif i in b: h-=1
print("chỉ số hạnh phúc của bạn ",h)
