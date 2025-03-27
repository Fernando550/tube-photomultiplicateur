import matplotlib.pyplot as plt
import matplotlib.patches as patches


class ph_tube:
    def __init__(self, N=4, a=3, b=2, c=4, d=2, e=0.2, f=6):
        self.N = N
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f


    def draw_photocathode(self):
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