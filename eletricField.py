import matplotlib.pyplot as plt
import numpy as np
from vectorfield import VectorField2D


class eletric_field:
    def __init__(self, surface, U=None, V=None):
        # super().__init__(surface, U, V)

        self.domain = surface
        self.Ex, self.Ey = self.trasform_to_eltricfield()
        self.X, self.Y = self.generate_meshgrid()
        self.field_magnitude = 1

        self.quiver_axes = None

    @property
    def magnitude(self):
        return np.sqrt(self.Ex*self.Ex+self.Ey*self.Ey)

    def trasform_to_eltricfield(self):
        field = np.fliplr(self.domain)
        dy, dx = np.gradient(field, 10)
        return (-dx, -dy)
    
    def generate_meshgrid(self):
        x = np.linspace(0, self.domain.shape[1] - 1, self.domain.shape[1])
        y = np.linspace(0, self.domain.shape[0] - 1, self.domain.shape[0])
        X, Y = np.meshgrid(x, y)
        return (X, Y)
    
    def normalise_vectors(self, U, V):
        lengths = np.sqrt(U**2 +V**2)

        lengths[lengths == 0] = 1

        U_norm = U / lengths
        V_norm = V / lengths    
        return U_norm * self.field_magnitude, V_norm * self.field_magnitude
    
    def vector_field_reduced(self):
        step = 4

        X_sub = self.X[::step, ::step]
        Y_sub = self.Y[::step, ::step]
        Ex_sub = self.Ex[::step, ::step]
        Ey_sub = self.Ey[::step, ::step]

        return X_sub, Y_sub, Ex_sub, Ey_sub
    
    def xy_mesh(self, xo=0, yo=0):
        """
        Les np.arrays X,Y du meshgrid, mais relatif à l'origine (xo, yo).
        Ceci permet d'utiliser directement les valeurs pour le calcul du
        champ d'une charge unique.

        Par défaut, l'origine est à (0,0)
        """
        X,Y = self.X-xo, self.Y-yo
        return X,Y

    def show(self):
        plt.figure(figsize=(19,6))
        X_sub, Y_sub, Ex_sub, Ey_sub = self.vector_field_reduced()
        U, V = self.normalise_vectors(Ex_sub, Ey_sub)
        plt.quiver(X_sub, Y_sub, U, V, cmap="viridis_r")
        plt.title("Eletric Vector Field")
        plt.gca().invert_yaxis()  
        plt.show()

    def display(self, use_color=True, title=None):
        # self.validate_arrays()

        if self.quiver_axes is None:
            self.quiver_axes = plt.subplot(1,1,1)
            self.quiver_axes.tick_params(direction="in")

        self.quiver_axes.cla()

        X,Y = self.xy_mesh()

        if use_color:
            """
            Au lieu de prendre la longueur de la fleche pour représenter
            la force du champ, je garde les fleches de la meme longueur
            et je les colore en fonction de la force du champ.

            Je dois gérer lorsque la longueur du vecteur est nulle, car on 
            tente de normaliser un vecteur nul, ce qui n'est pas possible.
            Cependant, si je mets lengths == 1, j'aurai simplement U/length == 0
            et V/lengths == 0 donc ce sera ok.
            """

            lengths = self.magnitude

            null_field = (lengths == 0)
            lengths[null_field] = 1

            U = self.Ex/lengths
            V = self.Ey/lengths

            
            """
            Les couleurs sont biaisées car il y a souvent des valeurs tres grandes.
            PLutot que de normaliser sur la plus grande valeurs, je limite
            les valeurs entre les percentiles 10-90 et je normalise la longueur des fleches.
            Ca fait plus beau.
            """
            percentile_10th = np.percentile(lengths, 10)
            percentile_90th = np.percentile(lengths, 90)
            colors = np.clip(lengths, a_min=percentile_10th, a_max=percentile_90th)

            """
            Et finalement, j'ai compris que les unités du champ sont plus simple
            lorsqu'on prend relatif a la grandeur du graphique: la largeur
            de la fleche sera aussi mieux adaptée independamment des unités.
            """
            self.quiver_axes.quiver(X, Y, U, V, colors, cmap="viridis_r")
        else:
            self.quiver_axes.quiver(X, Y, self.U, self.V)

        self.quiver_axes.set_aspect('equal')
        # plt.xlim(self.X.max(), self.X.min())  # Flip X-axis explicitly
        # plt.ylim(self.Y.min(), self.Y.max())  # Optional: preserve Y direction
        plt.gca().invert_xaxis()
        plt.title(title)
        plt.show()
        self.quiver_axes = None
        