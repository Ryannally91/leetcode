def decryptPassword(s):
    # Write your code here
    
    count_for_removal = 0
    #covert list to string at end
    j = 0
    s =list(s)
    for i in range(len(s)-1, -1, -1):
        # if s[i] == '0' or s[i] == '*':
        # print(s[i])
        if s[i]  == '0':
            s[i], s[j] = s[j], s[i]
            s.pop(j)
        print(s)
        if s[i] =='*':
            s[i-1], s[i-2] = s[i-2],  s[i-1]
            s.pop(i)
    s = ''.join(s)
    print(s)
    return s

decryptPassword('43Ah*ck0rr0nk')


print(type(5))