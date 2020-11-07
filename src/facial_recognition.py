"""
Author : Arnold Yeung

Main functions for facial recognition service.
"""

from PIL import Image
import pickle as pk
import numpy as np

import joblib

from image_tools import convert_bytes_to_image

def load_and_resize_image_file(file, size=(37, 50), greyscale=True, outfile=None):
    """
    Loads an image file into a PIL.Image object and resize.
    """
    img = Image.open(file)
    if greyscale:
        img = img.convert("L")
    img = img.resize(size=size, resample=Image.ANTIALIAS)

    if outfile:
        img.save(outfile)
    
    return img


def load_model(file):
    """
    Load a .pkl file containing a Scikit-Learn object into a variable.
    Arguments:
        - file (str) :        file containing Scikit-Learn object
    Returns:
        - model :             Scikit-Learn object
    """
    try:    
        model = joblib.load(file)
    except:
        st.write("Cannot load " + str(file) + ". Please make sure Scikit-Learn is 0.22.2.")
        raise ValueError("File incompatible with Scikit-Learn version.")

    return model

def recognize_face(clf, pca, image):
    """
    Runs the facial recognition inference pipeline.
    Arguments:
        - clf :                 Scikit-Learn object containing the classification model
        - pca :                 Scikit-Learn object containing the PCA transformer
        - image (ABImage) :     ABImage object containing data (bytes) and other attributes
            - data (byte) :     byte data of image (e.g., pixel values)
            - width (int) :     number of pixels wide
            - height (int) :    number of pixels tall
            - color (bool) :    whether image is colored (or greyscale) 
    Returns:
        - prediction (int) :    Predicted class of the image  
    """

    img = convert_bytes_to_image(image.data, image.width, image.height, image.color)

    #   convert to greyscale
    if image.color:
        img = img.convert("L")

    #   convert to numpy
    img_data = []
    for row in range(0, 50):
        for col in range(0, 37):
               img_data.append(img.convert("L").getpixel((col, row)))
    img_data = np.array([img_data])

    img_data = pca.transform(img_data)
    prediction = clf.predict(img_data)[0]
    
    return prediction

def get_target_name(class_num, target_names):
    """
    Get the corresponding target name for a given class number.
    Arguments:
        - class_num (int) :                     class number
        - target_names (dict{str:str, }) :      dictionary containing class numbers and target names
    Returns:
        - (str) : target name
    """
    try:
        return target_names[str(class_num)]
    except:
        raise KeyError("Cannot find corresponding target name for class number.")




if __name__ == '__main__':
    print("hellow world")