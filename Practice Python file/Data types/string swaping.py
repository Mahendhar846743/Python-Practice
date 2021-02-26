def swap_case(s):
    #use swapcae() method to display lower to upper and upper to lower
    return s.swapcase()

if __name__ == '__main__':
    #Take the user input
    s = input()
    #call the function
    result = swap_case(s)
    #Dispay the results
    print(result)