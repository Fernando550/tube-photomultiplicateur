import numpy as np
import matplotlib.pyplot as plt
from eletricField import eletric_field

# Constantes physiques
charge_electron = -1.602176634e-19  # C
masse_electron = 9.10938356e-31     # kg

class particle_motion:
    def __init__(self, electric_field: eletric_field, x0=0, y0=0, vx0=0, vy0=0,
                 charge=charge_electron, masse=masse_electron):
        self.E = electric_field
        self.charge = charge
        self.masse = masse
        self.position = np.array([x0, y0], dtype=float)
        self.velocity = np.array([vx0, vy0], dtype=float)
        self.trajectory = [self.position.copy()]
        self.time = 0
        self.dt = 1e-11  # pas de temps en secondes
        self.dynode_regions = []  # Pour la gestion des rebonds

    def get_acceleration(self, x, y):
        Ex, Ey = self.E.get_vector_at(x, y)
        return np.array([Ex * self.charge / self.masse,
                         Ey * self.charge / self.masse])

    def euler_step(self):
        a = self.get_acceleration(*self.position)
        self.velocity += a * self.dt
        self.position += self.velocity * self.dt
        self.time += self.dt
        self.trajectory.append(self.position.copy())

    def calculate_trajectory(self, max_steps=10000, detect_dynodes=False):
        """Calcule la trajectoire avec option de rebond"""
        for _ in range(max_steps):
            if self.is_out_of_bounds():
                break
                
            self.euler_step()
            
            if detect_dynodes:
                self._handle_dynode_collision()

    def _handle_dynode_collision(self):
        """Gestion des rebonds sur dynodes (question 3b)"""
        for dynode in self.dynode_regions:
            x_min, x_max = dynode['x_range']
            y_min, y_max = dynode['y_range']
            
            if (x_min <= self.position[0] <= x_max and 
                y_min <= self.position[1] <= y_max):
                self.position[1] += dynode['bounce']  # Rebond de 2mm
                self.velocity[1] *= -0.5  # Inversion avec perte d'énergie
                break

    def is_out_of_bounds(self):
        x, y = self.position
        X, Y = self.E.X, self.E.Y
        return (x < X.min() or x > X.max() or 
                y < Y.min() or y > Y.max())

    @property
    def trajectory_points(self):
        """Retourne les points de trajectoire en mm"""
        return np.array(self.trajectory)