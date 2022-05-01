'''given a matrix.  row and column reprsent users.  see how many connected groups their are'''

def countGroups(matrix):
    connections= {}
    for i in range(len(matrix)):
        print(i)
        for j in range(len(matrix[i])):
            print(j, '..', matrix[i][j])
            if i!=j:
                print('here')
                if matrix[i][j]=='1':
                    print('im here')
                    connections[i] = j
    print(connections)
    return len(connections)

countGroups(['110','110','110'])