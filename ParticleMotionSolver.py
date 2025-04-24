import numpy as np
import matplotlib.pyplot as plt


charge_electron = -1.602176634e-19
masse_electron = 9.1093837e-31

#domain --> tube

class particle_motion:
    def __init__(self, eletric_field, x0=0, y0=0, charge=charge_electron, masse=masse_electron):

        self.eletric_field = eletric_field
        self.charge = charge
        self.masse = masse
        self.position = (x0, y0)
        self.velocity = np.array([0, 0], float)
        self.acceleration = np.array([0, 0], float)
        

        self.dt = 1e-9
        self.iterations = 100000
        self.trajectory = []
        self.euler_path = []                               

        self.domain = eletric_field.domain.shape
        
  
    def method_of_euler(self):
        x, y = self.position
        Ex, Ey = self.eletric_field.get_vector_at(x, y)

        force_vector = np.array([Ex, Ey])*self.charge  #force 
        acceleration = force_vector/self.masse

        v0 = self.velocity

        self.velocity = self.velocity + self.dt * acceleration

        self.position = self.position + self.dt * v0

        return self.position

    
    def euler_trajectory(self):
        steps = 0
        x, y = self.position
        self.trajectory.append((x, y))

        while steps <= self.iterations:
            xf, yf = self.method_of_euler()
            self.trajectory.append((xf, yf))
            steps += 1

    def X(self, t=0):
        position = int(t*self.dt)
        return self.trajectory[position]

    def draw_path(self):
        # self.make_trajectory()
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

    

    
    