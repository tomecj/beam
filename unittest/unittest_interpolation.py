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


class TestInterpolation(unittest.TestCase):

    def test_lagrange_polynomialnomial(self):
        correct = np.array([[ 0.195, -0.105],
                            [ 0.91 ,  0.91 ],
                            [-0.105,  0.195]])
        u = intp.lagrange_polynomial(degree=2, eval_pts=[-0.3,0.3])
        self.assertTrue(np.allclose(u, correct, rtol=1e-10))

    def test_lagrange_polynomial_derivative(self):
        correct = np.array([[-0.8, -0.2],
                            [ 0.6, -0.6 ],
                            [ 0.2,  0.8]])
        u = intp.lagrange_polynomial_derivative(degree=2, eval_pts=[-0.3,0.3])
        self.assertTrue(np.allclose(u, correct, rtol=1e-10))
    
    def test_lagrange_polynomial_2_derivative(self):
        correct = np.array([[ 1.0,  1.0],
                            [-2.0, -2.0],
                            [ 1.0,  1.0]])
        u = intp.lagrange_polynomial_2_derivative(degree=2, eval_pts=[-0.3,0.3])
        self.assertTrue(np.allclose(u, correct, rtol=1e-10))
    
    def test_lagrange_polynomial_3_derivative(self):
        correct = np.zeros((3,2))
        u = intp.lagrange_polynomial_3_derivative(degree=2, eval_pts=[-0.3,0.3])
        self.assertTrue(np.allclose(u, correct, rtol=1e-10))

    def test_dual_basis_function(self):
        correct = np.array([-0.25, 1.5, -0.25])
        u = intp.dual_basis_function(2, 0)
        self.assertTrue(np.allclose(u, correct, rtol=1e-10))

if __name__ == '__main__':
    unittest.main()