a=8
m=(2*a)-2
for i in range(0,a):
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        print("* ",end=" ")
    print()
