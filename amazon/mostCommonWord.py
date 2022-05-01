


def mostCommonWord(paragraph, banned ):
    sanitize_str = ''.join(char.lower() if char.isalpha() else ' ' for char in paragraph)
    words = sanitize_str.split()
    print(words)
    word_count= {}
    for word in words:
        if word not in banned:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1

    return max(word_count, key=word_count.get)
        
      
print(mostCommonWord('hit hit??#@$ up and you love. it up up', ['up']))