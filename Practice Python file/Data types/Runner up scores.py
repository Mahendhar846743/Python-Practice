#Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score.

#1.Total participates in the game
N=int(input())
#2Initialize the List
S=[]
#3Repeat the section for scores
for i in range(N):
    #4.Each player score
    x=input()
    #5.put it into a list
    S.append(x)
#6.remove dublicate element from the list
y=set(S)
z=list(y)
#7.sort the list in reverse order
z.sort(reverse=True)
#8.Select the 2nd element from the list
print(z[1])

