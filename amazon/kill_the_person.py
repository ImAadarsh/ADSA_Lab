#Kill The Man Problem
def Josh(person, k, index):
    # Base case , when only one person is left
    if len(person) == 1:
        print(person[0])
        return

    # find the index of first person which will die
    index = ((index+k)%len(person))

    # remove the first person which is going to be killed
    person.pop(index)

    # recursive call for n-1 persons
    Josh(person,k,index)


n = 14 # specific n and k values for problem
k = 5
k-=1 # (k-1)th person will be killed
#
index = 0

# fill the person vector
person=[]
for i in range(1,n+1):
    person.append(i)    

Josh(person,k,index)

