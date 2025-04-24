import matplotlib.pyplot as plt
import matplotlib.patches as patches
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
        if positions is None:
            positions = self.set_dynodes_positions()

    # Mettre TOUTE l'enceinte à 0V (bords haut/bas/gauche/droite)
        self.values[0,:] = 0    # Bord haut
        self.values[-1,:] = 0   # Bord bas
        self.values[:,0] = 0    # Bord gauche
        self.values[:,-1] = 0   # Bord droit

    # Appliquer les tensions des dynodes
        dynodes_voltages = my_tools.set_voltage_dynodes(self.n_dynodes)
        w = int(self.dynode_width * self.h)
        h = int(self.dynode_height * self.h)

        self.values[:,-1] = (len(dynodes_voltages) + 1) * 100.0 

        for i in range(len(dynodes_voltages)):
            a = int(positions[i][0])
            b = int(positions[i][1])
            self.values[b:b+h, a:a+w] = dynodes_voltages[i]
            self.add_boundary_condition((slice(b, b+h), slice(a, a+w)), dynodes_voltages[i])

    def show_with_trajectory(self, trajectory_points, title="Trajectoire électronique"):
        """Affiche le potentiel existant avec trajectoire superposée"""
        plt.figure(figsize=(19, 6))
    
    # 1. Affichage du potentiel (identique à solve_laplace_by_relaxation)
        plt.imshow(self.values.T,
                  origin='lower',
                  cmap='viridis',
                  extent=[0, self.width, -self.height//2, self.height//2])
        plt.colorbar(label='Potentiel (V)')
    
    # 2. Superposition trajectoire
        traj = np.array(trajectory_points)
        plt.plot(traj[:,0], traj[:,1], 'r-', linewidth=2, label='Trajectoire')
        plt.scatter(traj[0,0], traj[0,1], c='yellow', s=100, marker='*', label='Émission')
    
    # 3. Configuration identique
        plt.title(title)
        plt.xlabel("Position x (mm)")
        plt.ylabel("Position y (mm)")
        plt.gca().invert_yaxis()
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

    def get_dynode_regions(self):
        """Retourne les régions des dynodes pour la détection de collision"""
        return [{
            'x_range': (x, x + self.dynode_width),
            'y_range': (y, y + self.dynode_height),
            'bounce': 2.0 if i % 2 == 0 else -2.0  # Alternance haut/bas
        } for i, (x,y) in enumerate(self.dynodes_positions)]

