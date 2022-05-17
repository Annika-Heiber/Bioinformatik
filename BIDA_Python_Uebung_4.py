def ausgabe(wert1, wert2):
    print("Ausgabe von Text aus einer Funktion")
    print(wert1)
    print(wert2)

ausgabe("Hello World", "  ")


def ausgabe( *mehrereParameter, ):
    print(7)
    for einzelwert in mehrereParameter:
        print(einzelwert)
        
ausgabe("Hallo", "Welt", "guten", "Morgen")

eingabe = input("Ihre Eingabe? ")


def my_sum(x,):
    result = 0
    for i in range(begin,end):
        result += x
        x += 1
print(result)
    