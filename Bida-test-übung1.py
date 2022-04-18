# 1 inch entspricht 2,45 Zentimeter 
# (a) 2 inch
# (b) 50 inch 
# (c) 92,7 inch

#n = 2
inch_wert = int(input("Gib einen Wert in inch ein "))

def inch_to_cm(inch): 
    return inch * 2.45  #n


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



# bei der variante mit der eingabe von n komm 4.9 raus ??
# bei der variante mit inch wert eingeben kommt 12.25 raus 


