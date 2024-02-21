q=str(input())
a=" a,i,o,u,e,A,I,O,U,E"
count=0
for i in q:
    if i in a:
        count+=1

print(count)
