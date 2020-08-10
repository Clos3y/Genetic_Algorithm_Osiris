import numpy as np
from generationclass import Generation
from PlottingFile import data_plotter, data_saver
import operator


if __name__ == "__main__":

    gen_list = []
    new_gen = True
    current_gen = 0
    max_gen = 12                   #Will have that many gens, eg. 4 = 4 gens (0-3)
    individuals_history = []
    
    gen_x_axis = []
    merit_y_axis = []
    data = [] 

    #Loops for the number of gens.
    while new_gen == True:

        #Keeps looping as new gens get added.
        for i in range(max_gen):
            gen_list.append(Generation(gen=current_gen))
            if i == 0:
                gen_list[i].populate(individuals_history)
            else:
                gen_list[i].repopulate(gen_list[i-1].newborn)
            data_saver(gen_list[i], gen_x_axis, merit_y_axis, data)
            gen_list[i].output_current_status()
            data_plotter(gen_x_axis, merit_y_axis)
            gen_list[i].mating_stage(individuals_history)
            current_gen += 1
            
            #Checks if the limit for the gens has been reached.
            #Exits loop when limit reached.
            if current_gen < max_gen:
                pass
            else:
                new_gen = False
                #Tells the user what the maximum merit achieved was.
                gen_list[i].population.sort(key=operator.attrgetter('merit'), reverse=True)
                print("The best simulation parameters achieved were:")
                print(gen_list[i].population[0])
                break

    #Saves the data into a file.
    np.save("GAData", data, allow_pickle=True)   