"""
Author :    Arnold Yeung

Server for receiving requests and sending responses to clients.
python3 -m grpc_tools.protoc -I../proto --python_out=. --grpc_python_out=. ../proto/image.proto
"""

from concurrent import futures
import logging

import grpc

import image_pb2
import image_pb2_grpc

import os
import json

from image_tools import rotate_image, convert_image_to_ABImage
from facial_recognition import recognize_face, load_model, get_target_name

class ABImageService(image_pb2_grpc.ABImageServiceServicer):

    def __init__(self):

        #   initialize models and dictionary for service 2 ("special")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.clf = load_model(os.path.abspath(os.path.join(dir_path, '.', 
                                'facial_recognition/svm.pkl')))
        self.pca = load_model(os.path.abspath(os.path.join(dir_path, '.', 
                                'facial_recognition/pca.pkl')))
        with open(os.path.abspath(os.path.join(dir_path, '.', 
                                'facial_recognition/target_names.json'))) as json_file:
            self.target_names = json.load(json_file)

        print("SVM model: ", type(self.clf))
        print("PCA model: ", type(self.pca))
        print("Classes: ", self.target_names)

    def RotateImage(self, request, context):

        rotated_image = rotate_image(request)
        out_image = convert_image_to_ABImage(rotated_image, request.image.color)

        return image_pb2.ABImage(color=request.image.color,
                                data=out_image['data'], 
                                width=out_image['width'], 
                                height=out_image['height'])

    def RecognizeFace(self, request, context):
        
        prediction = recognize_face(self.clf, self.pca, request.image)
        prediction_name = get_target_name(prediction, self.target_names)
        print("Prediction: ", prediction_name)

        return image_pb2.ABCustomImageEndpointResponse(classification=prediction_name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_ABImageServiceServicer_to_server(ABImageService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
