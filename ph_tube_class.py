import matplotlib.pyplot as plt
import numpy as np
from scalarfield import ScalarField

import my_tools


'''
        Initialise le tube. 

        Arguments :
        N : nombre de dynodes dans le tube
        a : espacement entre les dynodes et les extrémités du tube (mm)
        b : espacement entre les dynodes et les côtés du tube (mm)
        c : longueur d'une dynode (mm)
        d : espacement entre les dynodes (mm)
        e : épaisseur d'une dynode (mm)
        f : largeur de la base du tube (mm)
        '''

class ph_tube:
    '''Le tube photomultiplicateur!'''
    def __init__(self, **settings):

        default = {
            "n_dynodes": 4,
            "spacing": 3,
            "spacing_d_sides": 2,
            "dynode_width": 4,
            "spacing_dynodes": 2,
            "dynode_height": 0.2,
        }

        default.update(settings)

        for key, value in default.items():
            setattr(self, key, value)

        self.width = 19
        self.height = 6

        # delta h
        self.h = 0.1

        # boundary condition
        self.conditions = []                         
       
        self.matrix = np.zeros((int(self.height/self.h), int(self.width/self.h)))

    def set_dynodes_positions(self):
        positions = []
        for position in range(self.n_dynodes):

            pass
        return 

    def set_boundary_conditions(self):
        # List with all voltages of each dynode
        dynodes_voltages = my_tools.set_voltage_dynodes(self.n_dynodes)

        # Set the conditions of the right side of the tube
        self.matrix[:,-1] = (len(dynodes_voltages) + 1) * 100.0 
        

    def draw_photocathode(self):
        fig, ax = plt.subplots()
        ax.imshow(self.matrix, cmap='plasma', origin='lower',
          extent=[0, self.width/self.h, 0, self.height/self.h])

        ax.set_title("2D Visualization of Photomultiplier Tube")
        ax.axis('off')
        ax.set_xlim(0, self.width/self.h)
        ax.set_ylim(0, self.height/self.h)
        plt.show()


    

tube = ph_tube()
tube.set_boundary_conditions()
tube.draw_photocathode()