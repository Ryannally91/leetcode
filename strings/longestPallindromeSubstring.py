#two pointers 
#start at beginning, look left and right of current char, check if pallindrome
#continue

def longestPalindrome(s):
    if len(s)== 1:
        return s
    out = ''
    longest= 1

    for i in range(len(s)):
        #odd len
        l, r = i, i #start at beginning
        #check if pallendrome
        while l>= 0  and r < len(s) and s[l] == s[r]:
            print(l,'l--r', r)
            if (r-l +1 ) > longest:
                out = s[l:r+1]
                longest = r-l+1
            #expand pointers outward
            l-= 1
            r+= 1

        #even len
        l,r = i, i+1
        while l>= 0  and r < len(s) and s[l] == s[r]:
            if (r-l +1 ) > longest:
                out = s[l:r+1]
                longest = r-l+1
                
            l-= 1
            r+= 1
        return out

print(longestPalindrome('aabaade'))