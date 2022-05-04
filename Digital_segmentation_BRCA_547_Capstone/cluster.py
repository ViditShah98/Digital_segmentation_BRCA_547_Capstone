import cv2
import os
import sklearn
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def model(patch_path): 
    
    '''
    patch_path: path of the patch that model needs to be fitted.
    '''

    model = KMeans(n_clusters=8, max_iter=20,
                  n_init=3, tol=1e-3)
    fit_patch = plt.imread(patch_path)
    fit_patch_n = np.float32(fit_patch.reshape((-1, 3))/255.)
    model.fit(fit_patch_n)

    return model


def pred_and_cluster(model, dir_path):
    
    '''
    model: model that will be used to predict the patch.
    dir_path: path of the directory that has patches that needs to be predicted and clustered.
    
    '''
    for file in os.listdir(dir_path):
        
        try:
            os.mkdir(file[:-4])
        except:
            pass
        pred_patch = plt.imread(os.path.join(dir_path, file))
        pred_patch_n = np.float32(pred_patch.reshape((-1, 3))/255.)
        labels = model.predict(pred_patch_n)
        overlay_center = np.copy(model.cluster_centers_)
        back_img = np.uint8(np.copy(pred_patch))
        #Reassigning Overlay colors
        overlay_center[0] = np.array([255, 102, 102])/255. #Light Red
        overlay_center[1] = np.array([153, 255, 51])/255. #Light Green
        overlay_center[2] = np.array([0, 128, 255])/255. #Light Blue
        overlay_center[3] = np.array([0, 255, 255])/255. #Cyan
        overlay_center[4] = np.array([178, 102, 255])/255. #Light Purple
        overlay_center[5] = np.array([95, 95, 95])/255. #Grey
        overlay_center[6] = np.array([102, 0, 0])/255. #Maroon
        overlay_center[7] = np.array([255, 0, 127])/255. #Bright Pink
        #Ovrlaying each and every cluster
        for i in range(len(overlay_center)):
            seg_img = np.copy(pred_patch_n)
            seg_img[labels.flatten() == i] = overlay_center[i] 
            seg_img[labels.flatten() != i] = np.array([255, 255, 255])/255.
            seg_img = seg_img.reshape(pred_patch.shape)
            plt.imsave(os.path.join(file[:-4], 'segmented_'+str(i)+'.jpg'), seg_img, dpi=1000)
            seg_img = np.uint8(seg_img*255.)
            overlay_img = cv2.addWeighted(back_img, 0.4, seg_img, 0.6, 0)/255.
            plt.imsave(os.path.join(file[:-4], '_overlay_'+str(i)+'.jpg'), overlay_img, dpi=1000)
        #Make a complete cluster
        all_cluster = overlay_center[labels.flatten()].reshape(pred_patch.shape)
        plt.imsave(os.path.join(file[:-4], 'all_cluster.jpg'), all_cluster, dpi=1000)
        #Overlaying the complete cluster
        seg_img = np.uint8(np.copy(all_cluster)*255.)
        overlay_img = cv2.addWeighted(back_img, 0.6, seg_img, 0.4, 0)
        plt.imsave(os.path.join(file[:-4], 'full_overlay.jpg'), overlay_img, dpi=1000)

    return None