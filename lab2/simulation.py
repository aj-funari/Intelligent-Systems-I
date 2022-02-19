import numpy as np
import matplotlib.pyplot as ply

import Environment
import Prey
import plotting
import setup

#setup

environment, prey_list = setup.simulation_setup();

#main loop

number_of_time_steps = 100 ; 

#run main program loop

for n in range(0, number_of_time_steps):
  for i in range(0,len(prey_list) ):
    prey_list[i].eat(environment) ;
plotting.my_plots(environment,prey_list);
