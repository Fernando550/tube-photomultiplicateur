import ph_tube_class
from eletricField import eletric_field
from ParticleMotionSolver import particle_motion

def run():
    # 1. Calcul du potentiel
    tube = ph_tube_class.ph_tube()
    tube.set_boundary_conditions()
    tube.show(block=True)
    tube.solve_laplace_by_relaxation()
    tube.show(block=True)

    # 1. Calcul du champ électrique
    e_field = eletric_field(tube.values)
    e_field.display()
    
    # 3. Simulation trajectoire 
    electron = particle_motion(e_field, x0=0, y0=0)
    electron.calculate_trajectory()
    tube.show_with_trajectory(electron.trajectory_points)
    
    # 4. Rebonds
    electron.dynode_regions = tube.get_dynode_regions()  # Méthode à implémenter
    electron.calculate_trajectory(detect_dynodes=True)
    tube.show_with_trajectory(electron.trajectory_points, 
                            title="Trajectoire avec rebonds")

if __name__ == "__main__":
    run()