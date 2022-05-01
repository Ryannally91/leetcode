#USE recursion
import string

def reverseString(s, rev_str=''):
    rev_str= rev_str
    if s == '':
        return rev_str
    rev_str += s[-1:]
    print(rev_str, '>>', s)
    return reverseString(s[:-1], rev_str)
    #function is returning none when I didn't have return in front
    #Ask Ashish

    

print(reverseString('how are you'))


    # 1.make new str
    # add pop val to new string
    # 3. call function on popped string
    # 4. once og string is empty return new string

    # 'how are you?' >>>> '?'
    # 'how are you' >>>>> ' ?u'
