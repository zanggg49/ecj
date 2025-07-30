k = int(input("Nhap so phan tu k "))
a = [int(input(f"Nhan phan tu thu {i+1}: ")) for i in range(k)]
n = int(input("Nhap so dong n "))
m = int(input("Nhap so cot m "))
if n * m > k:
    print("no")
else:
    matran = []
    for i in range(n):
        hang = a[i * m : (i + 1) * m]
        matran.append(hang)
    print("Ma tran thu duoc ")
    for hang in matran:
        print(hang)
