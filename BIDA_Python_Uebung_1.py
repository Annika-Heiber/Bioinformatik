print("Hallo Welt")

a = 13 - 5 * 2 + 12 / 6
b = 6 + (27%5) * 3 
c = 1 / 2 - 1 / 4 + (4 + 3 / 8) * 2

print("Ergebnis =", a, b, c)

#Aufgaben 7. und 8. aus dem Übungsblatt

def calc_1():
    a = 13 - 5 * 2 + 12 / 6
    return a


def test_calc_1():
    # Check wether the function that is to be tested has been defined yet:
    if not "calc_1" in globals():
        print("The function 'calc_1' that is to be tested has not been defined yet")
    else:
        # Function has been defined, so test it:
        expected_result = 5
        actual_result = calc_1()
        if expected_result != actual_result:
            print("calc_1() gave result ", actual_result, ", but expected is ", expected_result)
        else:
            print("calc_1() worked as expected")

test_calc_1()

def calc_2():
    b = 6 + (27%5) * 3 
    return b

# Test the calc_2 function you will implement above:
def test_calc_2():
    # Check wether the function that is to be tested has been defined yet:
    if not "calc_2" in globals():
        print("The function 'calc_2' that is to be tested has not been defined yet")
    else:
        # Function has been defined, so test it:
        expected_result = 12
        actual_result = calc_2()
        if expected_result != actual_result:
            print("calc_2() gave result ", actual_result, ", but expected is ", expected_result)
        else:
            print("calc_2() worked as expected")

test_calc_2()

def calc_3():
    c = 1 / 2 - 1 / 4 + (4 + 3 / 8) * 2
    return c

# Test the calc_3 function you will implement above:
def test_calc_3():
    # Check wether the function that is to be tested has been defined yet:
    if not "calc_3" in globals():
        print("The function 'calc_3' that is to be tested has not been defined yet")
    else:
        # Function has been defined, so test it:
        expected_result = 9
        actual_result = calc_3()
        if expected_result != actual_result:
            print("calc_3() gave result ", actual_result, ", but expected is ", expected_result)
        else:
            print("calc_3() worked as expected")

test_calc_3()


#Aufgaben 9. und 10. aus dem Übungsblatt

#n = 2
inch_wert = int(input("Gib einen Wert in inch ein "))

def inch_to_cm(inch): 
    return inch * 2.54  #n


# Test the inch_to_cm function you will implement above:
def test_inch_to_cm():
    # Check wether the function that is to be tested has been defined yet:
    if not "inch_to_cm" in globals():
        print("The function 'inch_to_cm' that is to be tested has not been defined yet")
    else:
        # Function has been defined, so test it:
        inch_argument = 5
        expected_result = 12.7
        actual_result = inch_to_cm(inch_argument)
        if expected_result != actual_result:
            print("inch_to_cm() gave result ", actual_result, ", but expected is ", expected_result)
        else:
            print("inch_to_cm() worked as expected")


# Execute the above defined test of the inch_to_cm function:
test_inch_to_cm()
