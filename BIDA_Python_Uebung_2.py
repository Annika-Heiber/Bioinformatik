# Übungsaufgabe 2 aus Bioinformatischer Datenanalyse / Python. Vervollständigen
# Sie bitte dieses Script gemäß der Instruktionen. Führen Sie das script
# mittels der Kommandozeile aus `python3 BIDA_Python_Uebung_2.py`.
#
# TIP:
#-----
# Eine "Exception" (einen Fehler) erzeugt (engl: raise) man mit folgendem Befehl:
# raise Exception("Dimension-Error")


def matrix_mult(m1, m2):
    for i in range(len(m1)):
        for k in range(len(m2)):
            m[i][k] = m1[i][k] * m2[i][k]
    return m



def check_matrix(m):
    for i in range(1, len(m)-1):
        if not len(m[O]) == len(m[1]):
            raise Exception("Dimension-Error")                                
    else:
        print("korrekt")                                              
# Test the check_matrix function you will implement above:
def test_check_matrix():
    # Check wether the function that is to be tested has been defined yet:
    if not "check_matrix" in globals():
        print("The function 'check_matrix' that is to be tested has not been defined yet")
        # Warum steht hier ein 'return'? Was erspart das im folgenden Teil der
        # Funktion 'test_check_matrix'?0
        return

    # ======================================
    # Function has been defined, so test it:
    # ======================================
    m_false_1 = [[1,2], [1,2,3]]
    m_false_2 = [[1,2,3], [4,5]]
    m_correct_1 = [[1,2], [3,4]]
    m_correct_2 = [[1,2,3], [4,5,6], [7,8,9]]
    try:
        # Test one:
        check_matrix(m_false_1)
        # Test two:
        check_matrix(m_false_2)
    except Exception as error:
        if str(error) == "Dimension-Error":
            print("The function 'check_matrix' correctly raises a 'Dimension-Error' if the argument has incorrect dimensions.")
        else:
            print("The function 'check_matrix' does NOT raise a 'Dimension-Error' as expected.")
    # No error expected in the following code ...
    # ... test three:
    check_matrix(m_correct_1)
    # ... test four:
    check_matrix(m_correct_2)
    print("checkmatrix funktioniert")

# End of test_check_matrix


# Test the matrix_mult function you will implement above:
def test_matrix_mult():
    # Check wether the function that is to be tested has been defined yet:
    if not "matrix_mult" in globals():
        print("The function 'matrix_mult' that is to be tested has not been defined yet")
        return

    # ======================================
    # Function has been defined, so test it:
    # ======================================

    # Test whether function raises an error if dimensions are not correct:
    m_false = [[1,2], [1,2,3]]
    try:
        matrix_mult(m_false, m_false)
    except Exception as error:
        # Warum schreibt man 'str(error)' in der nächsten Zeile? Stichwort: Datentypen.
        if str(error) == "Dimension-Error":
            print("The function 'matrix_mult' correctly raises a 'Dimension-Error' if the two argument matrices cannot be multiplied.")
        else:
            print("The function 'matrix_mult' does NOT raise a 'Dimension-Error' as expected.")

    # Test matrix multiplication with itself:
    m1_test = [[0.8,0.15,0.05], [0.15,0.8,0.05], [0.05,0.05,0.9]]
    expected_result = [[0.6400, 0.0225, 0.0025], [0.0225, 0.6400, 0.0025], [0.0025, 0.0025, 0.8100]]

    actual_result = matrix_mult(m1_test, m1_test)
    if expected_result != actual_result:
        print("matrix_mult() gave result ", actual_result, ", but expected is ", expected_result)
    else:
        print("matrix_mult() worked as expected")

# End of test_matrix_mult


# Check whether a matrix is a probability matrix:
def check_probability_matrix(m):
    for row in m:
        if not len(row) == len(m):
            # Was macht das 'format' in der folgenden Zeile?
            print("Matrix 'm' is not quadratic. Found row with {0} cells, but 'm' has {1} rows.".format(len(row), len(m)))
            raise Exception("Dimension-Error")
        if not sum(row) == 1:
            print("Matrix 'm' is not a probability matrix. Found row that sums up to {0}, but expect that it sums to 1.".format(sum(row)))
            raise Exception("Non probability matrix. Row does not sum up to 1.0")
        # Hier fehlt noch ein Test; welcher könnte das sein?

# End of check_probability_matrix


# Execute the above defined tests:
test_check_matrix()
test_matrix_mult()
