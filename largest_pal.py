def isPalindrome(arg):
    for i in range(0, arg.length/2):
        if arg[i] != arg[arg.length-1-i]:
            return False
    return True

def longestPal(arg):
    max = arg[0]
    for i in range(0,arg.length-1):
        if (i+max.length) < arg.length:
            for j  in range(i+max.length,arg.length):
                temp = arg[i:j+1]
                if isPalindrome(temp):
                    max = temp
    return max

def findPal(arg,i,j):
    flag = 0
    while flag == 0:
        while arg[i] != "[a-z]":
            i -= 1
        while arg[j] != "[a-z]":
            j += 1
        if arg[i] == arg[j]:
            i-=1
            j+=1
        else:
            i+=1
            j-=1
            flag = 1
    
def test(arg):
    max = arg[0]
    for i in range(0, arg.length-3):
        j = i
        flag = 0
        if arg[i] == arg[i+1]:
            j += 1
            findPal(arg,i,j)
        elif arg[i] == arg[i+2]:
            j += 2
            findPal(arg,i,j)
        if max.length < (j-i):
            max = arg[i:j+1]
    return max