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
    
    
    
    
import matplotlib.pyplot as plt 
import numpy as np 
  
def create_plot(ptype): 
    
    x = np.arange(-10, 10, 0.01) 
      
    
    if ptype == 'sin': 
        
        y = np.sin(2*np.pi*x) 
    elif ptype == 'exp': 
        
        y = np.exp(-x) 
    elif ptype == 'hybrid': 
        
        y = (np.sin(2*np.pi*x))*(np.exp(-x)) 
              
    return(x, y) 
  
plt.style.use('ggplot') 
  
plt1 = plt.subplot2grid((11,1), (0,0), rowspan = 3, colspan = 1) 
plt2 = plt.subplot2grid((11,1), (4,0), rowspan = 3, colspan = 1) 
plt3 = plt.subplot2grid((11,1), (8,0), rowspan = 3, colspan = 1) 
  
x, y = create_plot('sin') 
plt1.plot(x, y, label = 'sine wave', color ='b') 
x, y = create_plot('exp') 
plt2.plot(x, y, label = 'negative exponential', color = 'r') 
x, y = create_plot('hybrid') 
plt3.plot(x, y, label = 'damped sine wave', color = 'g') 
  
plt1.legend() 
plt2.legend() 
plt3.legend() 
  
plt.show()
