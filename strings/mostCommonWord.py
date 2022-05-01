# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is 
# not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

#brute force

# Edge is capitalization comparing string and banned list>>>set both to lower
# punctutation >>> eliminate punctuation

#syntax for finding max value in a dictionary
def most_common(paragraph, banned):
    banned = list(map(lambda x: x.lower(), banned))
    paragraph = paragraph.split(" ")
    print(banned)
    words={}
    for word in paragraph: 
        word.lower
        if word in banned:
            continue
        elif word in words:
            words[word] += 1
        else:
            words[word] =1
    print(words)
    # most = max(list(words.values()))

    return max(words, key=words.get)  #there are several alternatives here
    

print(most_common('hi hi hi hey hey it is 12', ['HI']))

print(1 % 5)

pos, neg, is_0 = 0, 0, 0
print(neg, is_0, pos)
# print on seperate lines
print(pos,'\n', neg,'\n',is_0 )
# print(chr((ord('A')+ 5) % 90) + )


