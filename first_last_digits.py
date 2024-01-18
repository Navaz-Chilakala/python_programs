n=int(input())
li=[]
for i in range(n):
    x=input()
    li.append(x)
for i in range(n):
    print("first digit: "+li[i][0]+"last digit: "+li[i][-1])
