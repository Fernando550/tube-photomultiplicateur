import numpy as np
import matplotlib.pyplot as plt


# Constantes physiques
charge_electron = -1.602176634e-19  # C
masse_electron = 9.10938356e-31     # kg
scale_factor_x = 892.0159888
scale_factor_y = 12.31892056

class particle_motion:
    def __init__(self, electric_field, x0=0, y0=0, charge=charge_electron, masse=masse_electron):
        self.electric_field = electric_field
        self.charge = charge
        self.masse = masse

        self.position = (x0, y0)
        self.velocity = np.array([0, 0], float)
        self.acceleration = np.array([0, 0], float)
        

        self.dt = 1e-9
        self.iterations = 100000
        self.trajectory = [] 

        self.collision_points = self.get_colition_points()                             
        self.domain = electric_field.domain.shape
        
  
    def method_of_euler(self):
        x, y = self.position
        Ex, Ey = self.electric_field.get_vector_at(x, y)

        force_vector = np.array([Ex, Ey])*self.charge  #force 
        acceleration = force_vector/self.masse

        v0 = self.velocity

        self.velocity = self.velocity + self.dt * acceleration

        self.position = self.position + self.dt * v0
        
        return self.position

    
    def euler_trajectory(self):
        steps = 0
       
        while steps <= self.iterations:
            xf, yf = self.method_of_euler()
            self.trajectory.append((xf, yf))

            x, y = self.position
            position = self.convert_units(x, y)
            if self.dinode_colition(position):  # si l'electron touche un dynode fait ajoute 2 cm a la position en y
                self.position = (self.position[0], self.position[1] + 20*scale_factor_y)    
                self.euler_trajectory()
            steps += 1

    def X(self, t=0):
        position = int(t*self.dt)
        return self.trajectory[position]
    
    def dinode_colition(self, position):
        x, y = position
        position = (int(x), int(y))
        #return true if the electron touches a dynoe            
        if position in self.collision_points:
            return True
        else:
            return False
        

    def get_colition_points(self):
        conditions = self.electric_field.environment.conditions
        points = list()
        x_sh, y_sh = self.electric_field.environment.values.shape

        for (x_slice, y_slice), _ in conditions:
            x_range = range(*x_slice.indices(x_sh)) 
            y_range = range(*y_slice.indices(y_sh))

            for x in x_range:
                for y in y_range:
                    points.append((x, y - 40))

        return points
    
    def convert_units(self, x, y):
        return x / scale_factor_x, y / scale_factor_y

    def draw_path(self):

        self.euler_trajectory()
        x_vals, y_vals = zip(*self.trajectory)
        plt.figure(figsize=(19, 6))
        plt.plot(x_vals, y_vals, linestyle='-', color='blue', label='Electron Path')

        x_min = min(x_vals)
        plt.xlim(x_min, self.domain[1])

        plt.ylim(-30, 30)
        plt.axhline(0, color='gray', linestyle='--', linewidth=1)  
        plt.axvline(0, color='gray', linestyle='--', linewidth=1)  

        plt.xlabel("X Position")
        plt.ylabel("Y Position")
        plt.title("Electron Trajectory")
        plt.legend()
        plt.grid(True)
        plt.gca().set_aspect('equal') 
        plt.show()
