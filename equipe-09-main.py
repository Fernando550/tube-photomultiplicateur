import ph_tube_class
from eletricField import eletric_field


def run():
    #
    tube = ph_tube_class.ph_tube()
    tube.set_boundary_conditions()
    tube.show(block=False)
    tube.solve_laplace_by_relaxation()
    tube.show(block=False)

    e_field = eletric_field(tube.values)
    # e_field.display()
    e_field.show()
    

if __name__ == "__main__":
    run()