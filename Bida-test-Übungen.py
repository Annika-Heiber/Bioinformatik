m1 = [[8, 14, -6], 
      [12,7,4], 
      [-11,3,21]]

m2 = [[3, 16, -6],
           [9,7,-4], 
           [-1,3,13]]

m  = [[0,0,0],
       [0,0,0],
       [0,0,0]]


#To Multiply M1 and M2 matrices
for i in range(len(m1)):
    for k in range(len(m2)):
        m[i][k] = m1[i][k] * m2[i][k]

#To Print the matrix
print("The multiplication of Matrix m1 and m2 = ", m)


def check_matrix(m):
    if m1 is not m2:                                   #if range(lenm1) is not range(lenm2)
        raise Exception("Dimension-Error")                                
    else:
        print(m)                                              
# Test the check_matrix function you will implement above:
def test_check_matrix():
    # Check wether the function that is to be tested has been defined yet:
    if not "check_matrix" in globals():
        print("The function 'check_matrix' that is to be tested has not been defined yet")
        # Warum steht hier ein 'return'? Was erspart das im folgenden Teil der
        # Funktion 'test_check_matrix'?0
        return

test_check_matrix()

