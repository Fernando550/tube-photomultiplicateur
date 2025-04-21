import matplotlib.pyplot as plt

charge_electron = -1.602176634e-19
masse_electron = 5.48579909065e-4

class particle_motion:
    def __init__(self, eletric_field, x0=0, y0=0, charge=charge_electron, masse=masse_electron):

        self.eletric_field = eletric_field
        self.charge = charge
        self.masse = masse
        self.position = (x0, y0)
        self.accelaration = (0, 0)
        self.velocity = (0, 0)

        self.time_interval = 0.00001

        self.trajectory = [(x0, y0)]

        self.domain = eletric_field.domain.shape
        
    def get_force(self, x=None, y=None):
        if x == None or y == None:
            x, y = self.position
        
        Ex, Ey = self.eletric_field.get_vector_at(x, y)
        print(Ex, Ey)
        return Ex*self.charge, Ey*self.charge

    def get_accelaration(self, x, y):
        force_x, force_y = self.get_force(x, y)
        return force_x/self.masse, force_y/self.masse

    def get_new_velocity(self, ax, ay):
        v0x, v0y = self.velocity

        vx = v0x + (ax*self.time_interval)
        vy = v0y + (ay*self.time_interval)

        self.velocity = vx, vy

        return vx, vy

    def displacement(self, a0x, a0y, vx, vy):
        
        delta_x = vx*self.time_interval + (0.5*a0x*(self.time_interval**2))
        delta_y = vy*self.time_interval + (0.5*a0y*(self.time_interval**2))

        return delta_x, delta_y
  

    def make_trajectory(self, max_steps=10000):
        x_min, x_max = self.eletric_field.X.min(), self.eletric_field.X.max()
        y_min, y_max = self.eletric_field.Y.min(), self.eletric_field.Y.max()

        steps = 0
        while steps < max_steps:
            x0, y0 = self.position
            if not (x_min <= x0 <= x_max and y_min <= y0 <= y_max):
                break

            x0, y0 = self.position 
            ax0, ay0 = self.get_accelaration(x0, y0)
            vx, vy = self.get_new_velocity(ax0, ay0)
            delta_x, delat_y = self.displacement(ax0, ay0, vx, vy)
            self.trajectory.append((x0 + delta_x, y0 + delat_y))
            self.position = (x0 + delta_x, y0 + delat_y)
            self.time_interval += self.time_interval
            steps += 1

    def draw_path(self):
        self.make_trajectory()
        x_vals, y_vals = zip(*self.trajectory)

        plt.figure(figsize=(19, 6))
        plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='blue', label='Electron Path')

        x_min = min(x_vals)
        plt.xlim(x_min, self.domain[1])

        plt.ylim(-30, 30)
        plt.axhline(0, color='gray', linestyle='--', linewidth=1)  # Optional: show Y=0 line
        plt.axvline(0, color='gray', linestyle='--', linewidth=1)  # Optional: show X=0 line

        # Labels and title
        plt.xlabel("X Position")
        plt.ylabel("Y Position")
        plt.title("Electron Trajectory")
        plt.legend()
        plt.grid(True)
        plt.gca().set_aspect('equal')  # Optional: keep scale ratio realistic
        plt.show()