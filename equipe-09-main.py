import ph_tube_class
from eletricField import eletric_field
from ParticleMotionSolver import particle_motion

def run():
    # 1. Calcul du potentiel
    tube = ph_tube_class.ph_tube()
    tube.set_boundary_conditions()
    tube.show(block=False)
    tube.solve_laplace_by_relaxation()
    tube.show(block=False)


    e_field = eletric_field(tube)

    # 1. Calcul du champ électrique

    e_field.display()
    
    # 3. Simulation trajectoire 
    electron = particle_motion(e_field)
    electron.draw_path()
    

if __name__ == "__main__":
    run()