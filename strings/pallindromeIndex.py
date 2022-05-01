import unittest

def pallindromeIndex(s):
    # Write your code here
    for i in range(len(s)):
        _s = list(s)
        
        r = _s.pop(i)
        if len(_s) % 2== 0:
            if _s[:len(_s)//2] ==  sorted(_s[len(_s)//2+1:], reverse=True):
                print(i)
                return i
        else:
            right_side = _s[len(_s)//2 +1:]
            # print(right_side)
            right_reverse= list(reversed(right_side))
            # print(right_reverse)
            left_side=  _s[:(len(_s)//2 )]
            # print(left_side, '==', right_reverse)
            if left_side== right_reverse:
                # print(i)
                return i
                
    return False 

# print(pallindromeIndex('aabaca'))


class MainTest(unittest.TestCase):
    def test_pallindromeIndex(self):
        # self.assertEqual(pallindromeIndex('aabaca'), 4)
        self.assertEqual(pallindromeIndex('aacbaa'), 2)
        self.assertEqual(pallindromeIndex('zdfgsjfewfvnk'), False)
        

