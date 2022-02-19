# load libraries 
import numpy as np
import matplotlib.pyplot as plt

# Load our modules 
import Environment as env
import Prey as pr

# create a function that sets up everything 
def simulation_setup( size_x = 10, size_y = 10 , number_of_prey = 10  ):
	environment = env.Environment( size_x , size_y );
	environment.randomize(); 

	# define Prey (see above)
	prey_list = {}; 
	for i in range( 0, number_of_prey ):
		prey_list[i] = pr.Prey( environment ); 
		
	return environment, prey_list ; 
