import matplotlib.pyplot as plt
import numpy as np


class eletric_field:
    def __init__(self, surface, U=None, V=None):
        # super().__init__(surface, U, V)

        self.domain = surface
        self.Ex, self.Ey = self.trasform_to_eltricfield()
        self.X, self.Y = self.generate_meshgrid()
        self.field_magnitude = 1

        self.quiver_axes = None

        self.U = U
        self.V = V

    @property
    def magnitude(self):
        return np.sqrt(self.Ex*self.Ex+self.Ey*self.Ey)

    def trasform_to_eltricfield(self):
        field = self.domain
        dy, dx = np.gradient(field)
        return (-dx, -dy)
    
    def generate_meshgrid(self):
        height, width = self.domain.shape

        x = np.linspace(0, self.domain.shape[1], self.domain.shape[1])
        y = np.linspace(-height // 2, height // 2, height)
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

    def display(self, use_color=True, title="Electric Field"):

        if self.quiver_axes is None:
            self.quiver_axes = plt.subplot(1, 1, 1)
            self.quiver_axes.tick_params(direction="in")

        self.quiver_axes.cla()

        X, Y = self.xy_mesh()

        if use_color:
            lengths = self.magnitude.copy()
            lengths[lengths == 0] = 1

            U = self.Ex / lengths
            V = self.Ey / lengths

            percentile_10th = np.percentile(lengths, 10)
            percentile_90th = np.percentile(lengths, 90)
            colors = np.clip(lengths, percentile_10th, percentile_90th)

            quiv = self.quiver_axes.quiver(X, Y, U, V, colors, cmap="viridis_r")
        else:
            quiv = self.quiver_axes.quiver(X, Y, self.Ex, self.Ey)

        self.quiver_axes.set_aspect('equal')

        y_half_range = np.abs(self.Y).max()
        self.quiver_axes.set_ylim(-y_half_range, y_half_range)


        # plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
        # plt.axvline(0, color='black', linestyle='--', linewidth=0.5)

        plt.title(title)
        cbar = plt.colorbar(quiv, ax=self.quiver_axes)
        cbar.set_label('Vector Magnitude')

        plt.show()
        self.quiver_axes = None

    def get_vector_at(self, x=0, y=0):
        #cette partie du code a ete fait par chatgpt
        idx_x = (np.abs(self.X[0, :] - x)).argmin()
        idx_y = (np.abs(self.Y[:, 0] - y)).argmin()

        Ex_val = self.Ex[idx_y, idx_x]
        Ey_val = self.Ey[idx_y, idx_x]

        return Ex_val, Ey_val
                