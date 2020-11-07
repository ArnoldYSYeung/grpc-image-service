"""
Author : Arnold Yeung

Client to connect to server.
"""
from __future__ import print_function
import logging

import grpc

import image_pb2
import image_pb2_grpc

import os
import sys, getopt

from image_tools import convert_imagefile_to_ABImage, save_image, convert_image_to_ABImage, convert_bytes_to_image
from facial_recognition import load_and_resize_image_file

def parse_args(arguments):
    
    args_dict = {'service': 'rotation', 'color': False}

    for argument, value in arguments:
        if argument in ("-s", "--special"):
            args_dict['service'] = 'special'
        elif argument in ("-i", "--infile"):
            args_dict['infile'] = value
        elif argument in ("-o", "--outfile"):
            args_dict['outfile'] = value
        elif argument in ("-r", "--rotate"):
            args_dict['rotate'] = value
        elif argument in ("-c", "--color"):
            args_dict['color'] = True

    return args_dict

def run(args_dict):

    channel = grpc.insecure_channel('localhost:50051')
    stub = image_pb2_grpc.ABImageServiceStub(channel)

    if 'infile' in args_dict:
            input_file = args_dict['infile']
    else:
        input_file = input("Enter the image file: ")
    if not os.path.isfile(input_file):
        raise ValueError("File does not exist.")

    if 'color' in args_dict:
        output_rgb = args_dict['color']
    else:
        output_rgb = input("Is the input image colored? [y/n] ")
        if output_rgb in ["Y", "y"]:
            output_rgb = True
        else:
            output_rgb = False

    if  args_dict['service'] == 'rotation':

        if 'rotate' in args_dict:
            rotate_degree = int(args_dict['rotate'])
        else:
            rotate_degree = int(input("Select a rotation (0 = 0deg, 1 = 90deg, 2 = 180deg, 3 = 270deg): "))
        if rotate_degree not in [0, 1, 2, 3]:
            raise ValueError("Invalid rotation.")

        if 'outfile' in args_dict:
            output_file = args_dict['outfile']
        else:
            output_file = input("Enter the directory/name of the output image file: ")

        image = convert_imagefile_to_ABImage(input_file, rgb=output_rgb)

        response = stub.RotateImage(image_pb2.ABImageRotateRequest(rotation=rotate_degree, image=image))
        print("Width: ", response.width, "  Height: ", response.height)

        save_image(convert_bytes_to_image(response.data, response.width, response.height, response.color), 
                    output_file)

    elif args_dict["service"] == "special":
        
        if 'outfile' in args_dict:
            output_file = args_dict['outfile']
        else:
            output_file = None

        #   image is downsampled prior to sending to reduce bandwidth required
        img = load_and_resize_image_file(input_file, outfile=output_file)
        image = convert_image_to_ABImage(img, rgb=False)

        response = stub.RecognizeFace(image_pb2.ABCustomImageEndpointRequest(image=image))
        print("We recognize this to be an image of :", response.classification)
        
    else:
        raise ValueError("This service is unavailable.")

if __name__ == '__main__':
    logging.basicConfig()

    #   get arguments
    short_opts = "si:o:r:c"
    long_opts = ["special", "infile=", "outfile=", "rotate=", "color"]
    arguments = sys.argv[1:]

    try:
        arguments, _ = getopt.getopt(arguments, short_opts, long_opts)
    except getopt.error as err:
        print(str(err))
        sys.exit()

    run(parse_args(arguments))
