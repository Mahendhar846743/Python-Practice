def mutate_string1(string, position, character):
    # convert the string to list
    lst = list(string)
    # replace the given character in ith position
    lst[position] = character
    # convert list to string
    string = "".join(lst)

    return string
def mutate_string_slice(s,p,c):
    s= s[:p] + c + s[p+1:]
    return s

if __name__ == '__main__':
    #take input from user
    s = input()
    #take index and character
    i, c = input().split()
    #call the function
    s_new = mutate_string1(s, int(i), c)
    print(s_new)
    s_new2 = mutate_string_slice(s, int(i), c)
    print(s_new2)