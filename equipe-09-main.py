import ph_tube_class


def run():
    tube = ph_tube_class.ph_tube()
    tube.set_boundary_conditions()
    tube.show(block=False)
    tube.solve_laplace_by_relaxation()
    tube.show(block=True)

if __name__ == "__main__":
    run()