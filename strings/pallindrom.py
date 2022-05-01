

def isPalindrome(s):
    new = []
    for i in s.lower():
        if i.isalnum():
            new.append(i)
    print(new)

    if new == new[::-1]:
        return True
    return False

print(isPalindrome('RACe  a  caR'))


#optimized for max efficiency.  No extra memory being used
def isItPalindrome(s):
    s = ''.join(i for i in s.lower() if i.isalnum())
    print(s)
    return s == s[::-1]
        

print(isItPalindrome('RACe caR'))
