# given an array of string ints,  see if the permutaions of that number are divisible by 8.  return an array of yes or no
# ex.  [61, 75] >>> [yes, no] b/c  61 can turn to 16 which is divisible by 8

def checkDivisibility(arr):
    yes_or_no= []
    for n in arr:
        results = permutations(n)
        print('>>>',yes_or_no)
        print(results)
        isdivisible = False
        for result in results:
            print('>>>>', result)
            if int(result) % 8 == 0:
                # yes_or_no.append('YES')
                isdivisible= True
                break
        if isdivisible == True:
            yes_or_no.append('YES')
        else:
            yes_or_no.append('NO')
        
    return yes_or_no


def permutations(num):
    # perms=[]
    if len(num) == 1:
        return num
    # if len(num) == 2:
    #     perms.append(num)
    #     num[0], num[1] = num[1], num[0]
    #     perms.append(num)
    #     return perms
    perms= permutations(num[1:]) #this gives us number of all possible combos
    digit = num[0] 
    combos= []
    for perm in perms:
        for i in range(len(perm) + 1):
            combos.append(perm[:i] + digit + perm[i:])
    return combos

print(permutations('123'))

#why this works:
#uses recursion call statck
#https://www.youtube.com/watch?v=4lIQCoG4MnY

print(checkDivisibility(['123', '61', '75', '3']))