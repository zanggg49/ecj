n=int (input("nhap vao s phan tu n "))
list=[int (input (f"nhap phan tu thu {i+1} "))for i in range (n)]
x=int (input("nhap so x cann kiem tra: "))
print(f"so {x} xuat hien {list.count(x)} lan")
list[1:7]=[8, 5, 4, 0, 1, 3]
print("list moi khi thay the: ",list)
print("so lown nhat ", max(list))
print ("so nho nhat ",min(list))
y=int(input("nhap vao y can chen "))
list.insert(0,y)
print ("list sau khi chen y ",list)
if list ==sorted(list):
    print("tang")
elif list == sorted(lst, reverse=True):
    print("giam")
else: print("no")
