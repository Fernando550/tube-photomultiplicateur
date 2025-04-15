"""
Module for solving the Laplace equation using both CPU-based and GPU-accelerated solvers.

This module provides:
1. `LaplacianSolver`: Implements relaxation methods for solving the Laplace equation 
   in 1D, 2D, and 3D using iterative numerical approaches.
2. `LaplacianSolverGPU`: Extends `LaplacianSolver` to utilize GPU acceleration via 
   OpenCL, significantly improving performance for large arrays (no benefits for small 2D)

The GPU solver requires `pyopencl` and executes OpenCL kernels for parallelized 
computations on compatible hardware.

Dependencies:
- NumPy
- SciPy
- PyOpenCL (optional, required for `LaplacianSolverGPU`)
"""

import math
import numpy as np


from my_tools import left, center, right


class LaplacianSolver:
    """
    A CPU-based solver for the Laplace equation using relaxation methods.

    This class provides methods for solving the Laplace equation in
    1D, 2D, and 3D using iterative relaxation. The solver updates
    each grid point based on its neighboring values until convergence
    is reached.
    """

    def solve_by_relaxation(self, field, tolerance):
        """
        Selects the appropriate relaxation solver based on the field's dimensionality.

        Parameters:
        field (ScalarField): The field to be solved by the method of relaxation.
                             May contain an initial guess.
        tolerance (float): Convergence threshold.

        Returns:
        int: The number of iterations required for convergence.
        """

        if field.values.ndim not in [1, 2, 3]:
            raise ValueError("Unable to manage dimension > 3")

        if field.values.ndim == 2:
            return self.solve2D_by_relaxation(field, tolerance)


    def solve2D_by_relaxation(self, field, tolerance):  # pylint: disable=invalid-name
        """
        Solves the Laplace equation in 2D using iterative relaxation.

        Parameters:
        field (ScalarField): The 2D field to be solved. May contain an initial guess.
        tolerance (float): Convergence threshold.

        Returns:
        int: The number of iterations performed.
        """
        error = None
        field.apply_conditions()
        i = 0
        while error is None or error > tolerance:
            if i % 100 == 0:
                before_iteration = field.values.copy()

            field.values[center, center] = (
                field.values[left, center]
                + field.values[right, center]
                + field.values[center, left]
                + field.values[center, right]
            ) / 4
            field.apply_conditions()
            if i % 100 == 0:
                error = np.std(field.values - before_iteration)
            i += 1

        return i