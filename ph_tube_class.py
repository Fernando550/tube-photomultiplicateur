import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import Rectangle


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

        self.width = 19
        self.height = 6

        # delta h
        self.h = 0.1                         
        

        for key, value in default.items():
            setattr(self, key, value)
       

        self.grid = np.zeros((int(self.height/self.h), int(self.width/self.h)))
        print(np.shape(self.grid))

    def transformPosition(self, x, y):
        return (x/self.h, y/self.h)

    def made_Dinode(self, x, y):
        position = self.transformPosition(x, y)
        dynode = Rectangle(position, self.dynode_width, self.dynode_height, color='black')
        return dynode

    def draw_photocathode(self):
        fig, ax = plt.subplots()
        ax.imshow(self.grid, cmap='plasma', origin='lower',
          extent=[0, self.width/self.h, 0, self.height/self.h])

        # for i in range(self.n_dynodes):
        #     x = self.transformPosition()
        #     dynode = self.made_Dinode()
        #     ax.add_patch(dynode)
        
        ax.set_title("2D Visualization of Photomultiplier Tube")
        ax.axis('off')
        ax.set_xlim(0, self.width/self.h)
        ax.set_ylim(0, self.height/self.h)
        plt.show()

    def ph_visualaze(self):
        shape = (self.width, self.height)
        ph = np.zeros(shape=shape)

        plt.imshow(ph, cmap='viridis')
        plt.show()
        pass

    

tube = ph_tube()
tube.draw_photocathode()