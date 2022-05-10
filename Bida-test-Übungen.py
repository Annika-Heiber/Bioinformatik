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