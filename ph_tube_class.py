import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import Rectangle


class ph_tube:
    '''Le tube photomultiplicateur!'''
    def __init__(self, N=4, a=3, b=2, c=4, d=2, e=0.2, f=6, g=16):
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
        g : 
        '''
        self.n_dynodes = N
        self.spacing = a
        self.spacing_d_sides = b
        self.dynode_width = c
        self.spacing_dynodes = d
        self.dynode_height = e
        self.width = g
        self.height = f
        self.h = 0.1

    def make_grid_domain(self):
        return (int(self.height/self.h), int(self.width/self.h))

    def draw_photocathode(self):
        shape = self.make_grid_domain()
        image = np.zeros(shape, dtype=float)  
        fig, ax = plt.subplots()
        ax.imshow(image, cmap='plasma', origin='lower')

        for i in range(self.n_dynodes):
            x = self.spacing * (i + 1)
            y = self.height // 2 - self.dynode_height // 2 - ((-1)**i) * 30  # Zig-zag pattern
            dynode = Rectangle((x, y), self.dynode_width, self.dynode_height, color='black')
            ax.add_patch(dynode)
        
        ax.set_title("2D Visualization of Photomultiplier Tube")
        ax.axis('off')
        plt.show()

    def ph_visualaze(self):
        shape = (self.width, self.height)
        ph = np.zeros(shape=shape)

        plt.imshow(ph, cmap='viridis')
        plt.show()
        pass

    

tube = ph_tube()
tube.draw_photocathode()