s1 = input("chuoi s1: ")
s2 = input("chuoi s2: ")

print("dao s1:", s1[::-1])
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
s2_new = s2[:a] + s2[a:b+1][::-1] + s2[b+1:]
print("s2 sau khi dao tu a đến b:", s2_new)
s3 = ''.join([s1[i] for i in range(len(s1)) if i % 2 != 0])
print("s3 sau khi xoa vi tri :", s3)
s4 = ''
min_len = min(len(s1), len(s2))
for i in range(min_len):
    s4 += s1[i] + s2[i]
s4 += s1[min_len:] + s2[min_len:] 
print("s4 dan xen:", s4)
