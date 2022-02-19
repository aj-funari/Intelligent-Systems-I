import numpy as np
import matplotlib.pyplot as plt 

import Environment as env 

class Prey:
	def __init__( self , environment ):
		self.eating_rate = 0.05
		self.minimum_food = 0.05
		self.i = np.random.randint( 0 , environment.Food.shape[0])
		self.j = np.random.randint( 0 , environment.Food.shape[1])
        
	def eat( self , environment ):
		environment.Food[ self.i , self.j ] *= ( 1.0 - self.eating_rate )
		
