import ph_tube_class
from eletricField import eletric_field
from ParticleMotionSolver import particle_motion


def run():
    #
    tube = ph_tube_class.ph_tube()
    tube.set_boundary_conditions()
    tube.show(block=False)
    tube.solve_laplace_by_relaxation()
    tube.show(block=False)

    e_field = eletric_field(tube)
    e_field.display()

    eletron_motion = particle_motion(e_field)
    eletron_motion.draw_path()

    print(eletron_motion.X(3))

if __name__ == "__main__":
    run()