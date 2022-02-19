# import useful libraries
import numpy as np
import matplotlib.pyplot as plt

class Environment:
    def __init__( self, row,col ):
        self.Food = np.zeros( (row,col))
        for i in range(0,self.Food.shape[0]):
            for j in range(0,self.Food.shape[1]):
                self.Food[i,j] = 1.0; 
                
    def resize( self, newI, newJ ): 
        self.Food = np.zeros((NewI,NewJ))
        for i in range(0,self.Food.shape[0]):
            for j in range(0,self.Food.shape[1]):
                self.Food[i,j] = 1.0; 
                
    def randomize( self ):
        for i in range(0,self.Food.shape[0]):
            for j in range(0,self.Food.shape[1]):
                self.Food[i,j] = np.random.uniform();
    
    def plot_me( self): # here we could even add args and apply names to the figures
            plt.figure(); # this produces a new plot instead of overwriting the old  
            CS = plt.contourf( np.transpose(self.Food) );
 
