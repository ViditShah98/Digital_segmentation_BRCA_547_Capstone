import cluster
import unittest
import numpy as np

from cluster import model, pred_and_cluster, remove_background

# class pred_and_cluster(unittest.TestCase):
#     def test_smoke(self):
#         class model():
#             clys = np.random.randn(8, 3)
#         pred_and_cluster(model, os.getcwd())
#         return

class remove_background(unittest.TestCase):
    def test_smoke(self):
        slide_img = np.random.randint(0, 255, size=(20000, 30000, 3))
        remove_background(slide_img,8,8,color_delta=40)
        return

    def test_tile_size_integer(self):
        with self.assertRaises(TypeError):
            slide_img = np.random.randint(0, 255, size=(20000, 30000, 3))
            remove_background(slide_img,8.2,8,color_delta=40)
        return

    def test_y_tile_size_dim(self):
        with self.assertRaises(ValueError):
            slide_img = np.random.randint(0, 255, size=(20000, 30000, 3))
            remove_background(slide_img,8,20001,color_delta=40)
        return

    def test_y_tile_size_positive(self):
        with self.assertRaises(ValueError):
            slide_img = np.random.randint(0, 255, size=(20000, 30000, 3))
            remove_background(slide_img,8,-8,color_delta=40)
        return

    def test_x_tile_size_dim(self):
        with self.assertRaises(ValueError):
            slide_img = np.random.randint(0, 255, size=(20000, 30000, 3))
            remove_background(slide_img,30001,8,color_delta=40)
        return

    def test_x_tile_size_positive(self):
        with self.assertRaises(ValueError):
            slide_img = np.random.randint(0, 255, size=(20000, 30000, 3))
            remove_background(slide_img,-8,8,color_delta=40)
        return