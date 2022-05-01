# Given a two dimensional matrix of binary numbers find the number of continuous rectangles that are entirely based on zeros.
'''
[1,0,0,0,1],
[1,0,0,1,1]
'''

# ________________________________________________________________________


# 2. How to define classes to represent rubik's cube and implement some basic functionality like twist and is complete?

class Rub_Sq:
    def __init__(self, color):
        self.color = color
        self.position = None

    #6 3x3 matrixes
    [ [['red', 'blue', 'orange'],
    [ 'yellow', 'green', 'white' ],
    ['red', 'blue', 'orange']],
    [['red', 'blue', 'orange'],
    [ 'yellow', 'green', 'white'],
    ['red', 'blue', 'orange']] ,
    [['red', 'blue', 'orange'],
    [ 'yellow', 'green', 'white' ],
    ['red', 'blue', 'orange']]  ]
    def randomize_cube_create(self):
        # colors = ['red', 'blue', 'orange', 'yellow', 'green', 'white' ]
        colors = {'red': 9, 'blue': 9}

        #or use dictionary for placement {'red': face, row, col}
        positions= []
        for i in range(54):
            positions
        for color in colors:
            for j in range(9):
                num = random
                Rub_Sq(color,  )

    def left_front():
        pass
    # moves horizontal-front middle, back  vertical front mid back
    # def 
    


# ________________________________________________________________________

# Given a matrix find the top-left corner and bottom-right corner or
# find the top-left corner and the width and height of the rectangle
# made of 0's

def find(matrix):
    tl_br=[]
    tl_br.append(matrix[0][0])
    
    tl_br.append( matrix[(len(matrix)-1)][-1])
    return tl_br

print(find([['red', 'blue', 'orange'],
    [ 'yellow', 'green', 'white' ],
    ['red', 'blue', 'green']]))

# ________________________________________________________________________

# 2.5 Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an earlier node, so as to make a loop in the linked list.
# EXAMPLE
# input: A -> B -> C -> D -> E -> C [the same C as earlier]
# output: C

# ________________________________________________________________________

# MassDrop Interview Question:
# Given an integer print out asterisks up to that integer
# each separated by a newline
# for ex. n = 3 would output
# *
# **
# ***

# Use only recursion and no iteration involved for example you cannot print
# "*" two times there should only be one print("*") call

# Regular recursive way using iteration "trick"
# which was clarified that it is not allowed

def asterisks(num):
    if num == 0:
        return  #once it hits here it will return the stack
    else:
        asterisks(num - 1)   ##it will stack each call until nums equals 0, then will execute LIFO [1,2,3,4,5,] 
        print('*' * num)


asterisks(6)

# ________________________________________________________________________

