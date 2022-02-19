import numpy as np
import matplotlib.pyplot as plt 

import Environment as env 
import Prey as pr 

def my_plots( E , prey_list ):
	# plt.clf(); 
	E.plot_me(); 
	for n in range( 0, len(prey_list) ):
		plt.plot( prey_list[n].i , prey_list[n].j , 'wo', markersize=10 ) ; # , s=10,  mec='k' , mfc='w' )
	plt.axis('image')
