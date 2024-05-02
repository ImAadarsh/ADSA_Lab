#Print K largest(or smallest) elements in an array

list = [1,4,6,2,1,5,7,20,3]
k = 1
for i in range(k):
    for j in range(len(list)-1-i):
        if(list[j]>list[j+1]):
            list[j],list[j+1]=list[j+1],list[j]
print(list[len(list)-k])
        