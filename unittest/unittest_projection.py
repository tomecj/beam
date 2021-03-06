import os
import sys

cwd = os.getcwd()
folder = os.path.basename(cwd)
while folder != "beam":
    cwd = os.path.dirname(cwd)
    folder = os.path.basename(cwd)
    if len(cwd) == 0:
        print("Root directory was not found. Try inserting the path manually with 'sys.path.insert(0, absolute_path_to_root)'")
        sys.exit()
print("Root directory:", cwd)
sys.path.insert(0, cwd)

import unittest
import numpy as np
import interpolation as intp
import projection as proj


class TestProjection(unittest.TestCase):

    def test_nearest_point_projection_1(self):
        correct = np.array([0, 0, 0, 5])
        X = np.array([[0,    0,   0],
                      [10,   0,   0]]).T
        P = np.array( [5,    0,   5])
        interpolation_d0 = lambda x: intp.lagrange_polynomial(degree=X.shape[1]-1, eval_pts=x)
        interpolation_d1 = lambda x: intp.lagrange_polynomial_derivative(degree=X.shape[1]-1, eval_pts=x)
        interpolation_d2 = lambda x: intp.lagrange_polynomial_2_derivative(degree=X.shape[1]-1, eval_pts=x)
        u = proj.nearest_point_projection(
            interpolation_d0, interpolation_d1, interpolation_d2,
            X, P,
            s0=0, TOLER=1e-8, MAXITER=10
        )
        self.assertTrue(np.allclose(u, correct, rtol=1e-10))
    
    def test_nearest_point_projection_2(self):
        correct = np.array([-0.23045933, 0.38268789, -0.0406458, -0.4820473])
        X = np.array([[0,   0,   0  ],
                      [1,   0,   0.4],
                      [1.5, 0.4, 1.0],
                      [1.2, 1.0, 1.7]]).T
        P = np.array([1.5, 0.0, 0.0])
        interpolation_d0 = lambda x: intp.lagrange_polynomial(degree=X.shape[1]-1, eval_pts=x)
        interpolation_d1 = lambda x: intp.lagrange_polynomial_derivative(degree=X.shape[1]-1, eval_pts=x)
        interpolation_d2 = lambda x: intp.lagrange_polynomial_2_derivative(degree=X.shape[1]-1, eval_pts=x)
        u = proj.nearest_point_projection(
            interpolation_d0, interpolation_d1, interpolation_d2,
            X, P,
            s0=0, TOLER=1e-8, MAXITER=10
        )
        self.assertTrue(np.allclose(u, correct, rtol=1e-10))

if __name__ == '__main__':
    unittest.main()