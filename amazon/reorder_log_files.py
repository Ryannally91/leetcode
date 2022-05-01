##### Leetcode solution

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1) #maxsplit to only seperate identifier form rest of string
            #ex.  'id3 cat dog mouse' --> ['id3', 'cat dog mouse' ]  now we can compare the rest strings, then _id if needed
            return (0, rest, _id) if rest[0].isalpha() else (1, )

            #0 represents letter string (to differentiate for dig logs), then compare rest,  if rest is the same then compare id

        return sorted(logs, key=get_key)

# examples:
'''
sorted(student_objects, key=lambda student: (student.grade, student.age))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

this sorts by grade, then by age
'''

'''Time and Space complexity

Time Complexity: \mathcal{O}(M \cdot N \cdot \log N)O(M⋅N⋅logN)

First of all, the time complexity of the Arrays.sort() is \mathcal{O}(N \cdot \log N)O(N⋅logN), as stated in the API specification, which is to say that the compare() function would be invoked \mathcal{O}(N \cdot \log N)O(N⋅logN) times.

For each invocation of the compare() function, it could take up to \mathcal{O}(M)O(M) time, since we compare the contents of the logs.

Therefore, the overall time complexity of the algorithm is \mathcal{O}(M \cdot N \cdot \log N)O(M⋅N⋅logN).

Space Complexity: \mathcal{O}(M \cdot \log N)O(M⋅logN)

For each invocation of the compare() function, we would need up to \mathcal{O}(M)O(M) space to hold the parsed logs.

In addition, since the implementation of Arrays.sort() is based on quicksort algorithm whose space complexity is \mathcal{O}(\log n)O(logn), assuming that the space for each element is \mathcal{O}(1)O(1)). Since each log could be of \mathcal{O}(M)O(M) space, we would need \mathcal{O}(M \cdot \log N)O(M⋅logN) space to hold the intermediate values for sorting.

In total, the overall space complexity of the algorithm is \mathcal{O}(M + M \cdot \log N) = \mathcal{O}(M \cdot \log N)O(M+M⋅logN)=O(M⋅logN).'''

###similar to mine
def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for log in logs:
            if log.split()[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        def weirdOrder(log):
            all_parts = log.split()
            key, rest = all_parts[0], all_parts[1:]
            return ' '.join(rest) + ' ' + key
        letter_logs.sort(key=weirdOrder)
        return letter_logs + digit_logs


####My attempt
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterlogs={}
        diglogs = []
        for i in logs:
            new = i.split(' ')
            # print(new[1])
            if new[1].isalpha():
                letterlogs[new[0]] = new[1:]
            else:
                diglogs.append(new)
                
        sorted_letters = list(sorted(letterlogs.items(), key= letterlogs.get))
        print(sorted_letters)
        print(letterlogs, '---', diglogs)
        
        
        #split(' ')
        #check i[1],  sort so that letters are first
        # create two new lists append to letters,  append digits (no further sorting needed)
        # sort letters by contents letters[1:] to not include identifier
        #if condition for contents that are equal,  compare identifiers
        #combine sorted letters list and digits list
        
        #hashtbales
        