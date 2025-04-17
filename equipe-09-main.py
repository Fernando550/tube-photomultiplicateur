import ph_tube_class
from vectorfield import SurfaceDomain, VectorField2D


def run():
    #
    tube = ph_tube_class.ph_tube()
    tube.set_boundary_conditions()
    tube.show(block=False)
    tube.solve_laplace_by_relaxation()
    tube.show(block=False)

    x, y = tube.values.shape

    domain = SurfaceDomain(X=x, Y=y)
    
   


if __name__ == "__main__":
    run()