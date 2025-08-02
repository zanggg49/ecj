def kt(s):
    if len(s) == 0:
        return False
    for ch in s:
        if ch < '0' or ch > '9':
            return False
    return True
n=int(input("nhập số phần tử của mảng "))
a=[]
for i in range (n):
    s=input(f"nhập phần tử thứ {i+1} ")
    a.append(s)
    b=tuple(a)
    print ("tuple b: ",b,sep=" ")
    so=0
    for i in b:
        if kt(i):
            so+=1
    print("số phần tử dạng số ",so)
