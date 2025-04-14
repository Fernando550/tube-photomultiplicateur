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

class ph_tube(ScalarField):
    '''Le tube photomultiplicateur!'''
    def __init__(self, **settings):

        default = {
            "n_dynodes": 4,
            "spacing": 3,     #a espacement entre les dynodes et les extrémités du tube (mm)
            "spacing_d_sides": 2, #b espacement entre les dynodes et les côtés du tube (mm)
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
        self.h = 10
 

        self.dynodes_positions = [(3,2), (6,4), (9,2), (12,4)]                      
       
        super().__init__((self.height*self.h, self.width*self.h))

        

    def set_dynodes_positions(self):

        positions = []
        for a, b in self.dynodes_positions:
            positions.append(my_tools.shift_coords(a, b, self.h))

        return positions

    def set_boundary_conditions(self, positions=None):
        if positions == None:
            positions = self.set_dynodes_positions()

        # List with all voltages of each dynode
        dynodes_voltages = my_tools.set_voltage_dynodes(self.n_dynodes)

        # Set the conditions of the right side of the tube
        self.values[:,-1] = (len(dynodes_voltages) + 1) * 100.0 

        w = int(self.dynode_width * self.h)
        h = int(self.dynode_height * self.h)

        for i in range(len(dynodes_voltages)):
            a = int(positions[i][0])
            b = int(positions[i][1])
            self.values[b : b + h, a : a + w] = dynodes_voltages[i]


# tube = ph_tube()
# print(tube.values)
# tube.set_boundary_conditions()
# tube.show(block=True)