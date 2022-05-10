#print ("Bitte geben Sie Ihren Namen ein:", end=" ")
#print ("Annika")

#print ("name", "    " ,"vorname", "    " ,"alter", "    " ,"wohnort")

#x = str(input("Sag mir 'was Nettes "))
#print("Vielen Dank für deine Eingabe, die da war: ", x)

#import sys
#from termcolor import colored, cprint

#x = str(input(colored("Sag mir 'was Nettes:   ", 'red', attrs=['reverse', 'blink'])))ne
#print('Vielen Dank für deine Eingabe, die da war:', x, )



def ggt(a, b):
    
    if b==0:
        return a
    else:
        print(a,b)
        return ggt(b, a%b)
        
ggt(5,9)


def fakultät(n, a=1): 
    for i in range(1, n+1):
        a = a* i
    print(a)   
  
fakultät(5)
    
    