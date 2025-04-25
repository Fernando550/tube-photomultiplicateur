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

    # bonnus
    p = {
            "n_dynodes": 12,
            "spacing": 0,     
            "spacing_d_sides": 2,
            "dynode_width": 1.5,
            "spacing_dynodes": 1,
            "dynodes_positions": [(1,2), (2,4), (4,2), (5,4), (7,2), (8,4), (10,2), (11,4), (13,2), (14, 4), (16,2), (17, 4)],
        }

    new_tube = ph_tube_class.ph_tube(**p)
    new_tube.set_boundary_conditions()
    new_tube.solve_laplace_by_relaxation()
    new_tube.show(block=True)
    

if __name__ == "__main__":
    run()