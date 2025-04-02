import matplotlib.pyplot as plt
import matplotlib.patches as patches


class ph_tube:
    '''Le tube photomultiplicateur!'''
    def __init__(self, N=4, a=3, b=2, c=4, d=2, e=0.2, f=6):
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
        self.N = N
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f


    def draw_photocathode(self):
        '''Affiche le tube graphiquement.'''
        fig, ax = plt.subplots()
        tube = patches.Rectangle((0.5, 0.5), self.f, 4, edgecolor='black', facecolor='lightblue', linewidth=2)
        ax.add_patch(tube)

        # Set limits and aspect ratio
        ax.set_xlim(0, self.f + 1)  # or self.f + 0.5 for tight fit
        ax.set_ylim(0, 5.5)         
        ax.set_aspect('equal')

        # Show the plot
        plt.show()


tube = ph_tube()
tube.draw_photocathode()