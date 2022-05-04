#This code returns an overlay image of 8 clusters and the input image.
#Inorder to use this, 
#Step 1: Save in the same folder as jupyter notebook.
#Step 2: Render "import cluster" along with other libraries and call the function.


import os
import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib as mpl
import matplotlib.pyplot as plt

def overlay_image(img):
    
    '''
    img: input image --> np.ndarray
    return: overlay image of input and clusters --> np.ndarray
    '''
    
    img_new = np.float32(img.reshape((-1, 3)))
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 10, 0.1)
    attempts = 10
    inertia, labels, center = cv2.kmeans(img_new, 8, 
                                        None, criteria, 
                                        attempts, cv2.KMEANS_RANDOM_CENTERS)
    
    
    new_center = np.uint8(np.array([[255, 0, 0], [255, 128, 0], [0, 255, 0], [0, 153, 153], 
                           [0, 0, 102], [255, 0, 255], [255, 255, 0], [32, 32, 32]]))
    
    segmented_image = new_center[labels.flatten()].reshape(img.shape)
    
    final_image = cv2.addWeighted(img, 0.75,
                                 segmented_image, 0.35, 0)
    return final_image