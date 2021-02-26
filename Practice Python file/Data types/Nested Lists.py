if __name__ == '__main__':
    # enter the number of students
    nl1=[]
    for _ in range(int(input())):
        l1=[]
        #name of the student
        name = input()
        l1.append(name)
        #Score of the student
        score = float(input())
        l1.append(score)
        nl1.append(l1)
    #sorting the nested loop second item i.e item[1]
    nl1.sort(key=lambda item:item[1])
    #sepearating scores
    scores=[]
    for i in nl1:
        scores.append(i[1])
    #removing dublicates
    s1=set(scores)
    s2=list(s1)
    s2.sort()
    out=[]
    #compare the name
    for x in nl1:
        print(s2[1])
        if s2[1] in x:
            out.append(x[0])
    out.sort()
    # display the output
    for y in out:
        print(y)