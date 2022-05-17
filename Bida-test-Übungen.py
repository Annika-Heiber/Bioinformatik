# summe = 1+2+3+4+5 = 15
def my_sum(k,n):
    summe = 0

    while k <= n:
        summe = summe + k
        k = k+1 
    
    print(summe)

my_sum(0,2)


def report_named_argos(*mehrereParameter,):
    
    for einzelwert in mehrereParameter:
        print("Argument-Wert/Name:", sep = "-")
        print(einzelwert, sep = "-")
       
report_named_argos("hey", 7, "Müde", )


