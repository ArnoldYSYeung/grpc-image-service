# Overview

## Description 
This gRPC Python3 server for Ubuntu 18.04 runs two microservices:

- <strong>Rotation</strong>: an image file is rotated by a multiple of 90 degrees counter-clockwise and is saved as an output file
- <strong>Facial Recognition</strong>: an image file is classified to contain 1 of 2 individuals (George W. Bush and Colin Powell)

The facial recognition microservice is implemented using a SVM classifier from Scikit-Learn, trained on the <a href="http://vis-www.cs.umass.edu/lfw/">Labeled Faces in the Wild</a> dataset. The code for training this classifier is available <a href="https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html">here</a> (as a Scikit-Learn example). Please note that there are severe limitations to this classifier, which are discussed below.

## Setup
This setup guide applies for a fresh installation of Ubuntu 18.04:

1. Download and save this directory (and all contained files) in the desired location
2. Install Python3: `sudo apt install python3`
3. Install `pip`: `sudo apt-get update`
`sudo apt-get upgrade`
`sudo apt install python3-pip`
3. Upgrade `pip` for Python3: `python3 -m pip install --upgrade pip`
4. Install requirements.txt using `pip`: `python3 -m pip install -r requirements.txt` (NOTE: You may want to create a virtual environment)

If there are changes made to the `./proto/image.proto` or changes to the services or message classes in `./src/server.py` or `./src/client.py`, navigate to `./src/` and run the following to update `./src/image_pb2.py` and `./src/image_pb2_grpc.py`:

`python3 -m grpc_tools.protoc -I../proto --python_out=. --grpc_python_out=. ../proto/image.proto`

Note that our code places the server at an unsecure local port. This is for the convenience of deploying and testing the server locally. I highly recommend changing to a secure port (using `server.add_secure_port`) with credentials when deploying this externally.

## Instructions
To start the server, navigate to source directory using `cd ./grpc-image-service-prompt/src` and run the server using `python3 server.py`.

To run the client, in a separate terminal navigate to the source directory (see above) and run `client.py`.  Note that the client has several command line arguments that you may use. If a required command line argument is not entered, a prompt for its value would appear.

- `-s`: Indicates facial recognition service.  If not included, the image rotation service would run instead. (no value required)
- `-i`: Input image file to rotate or classify (e.g., `-i ../color_images/meme1.jpg`). (value required)
- `-r`: Rotation multiple of 90 degrees, only required for image rotation service (e.g., `-r 2`). (value required)
- `-o`: Output rotated image file for the rotation service or the downsampled, greyscale image used for classification for the facial recognition service (e.g., `-o ../out_images/rot_meme1.jpg`). (value required) 
- `-c`: Indicates that the input image is colored, and not greyscale. (no value required)

An example of running the rotation service: 

`python3 client.py -i ../color_images/meme1.jpg -r 2 -o ../out_images/rot_meme1.jpg -c`

An example of running the facial recognition service: 

`python3 client.py -s -i ../color_images/george.jpg -c`

## Discussion

### Image Rotation

This service rotates an inputted image by a multiple of 90 degrees. The outputted image is then saved at the desired location. On the client side, the image file is converted to into bytes in `ABImage` format and sent to the server, where the bytes is converted to a `PIL.Image` object. The image is then rotated using `PIL.Image.rotate()` method and sent back to the client as bytes in the `ABImage` format. The client then converts the bytes to a `PIL.Image` object which is saved as the output image file.

Note that due to the unary RPC used (limitations further discussed below), large images will be scaled down to 1000 pixels by 1000 pixels, while maintaining aspect ratio, in the client. This reduces the data size so that the entire image may be sent to the server as a single message. However, this means that the returned rotated image would also be scaled down to this size.

<img src="https://github.com/ArnoldYSYeung/grpc-image-service-prompt/blob/master/overview_images/rotation.png" alt="Rotation pipeline" width=500 />


### Facial Recognition

This service allows the recognition of faces in images for 2 individuals: George W. Bush and Colin Powell (they have the most images in the dataset). At the start of the server, a trained SVM classifier and a trained PCA transformer are loaded into the server from files `./src/facial_recognition/svm.pkl` and `./src/facial_recognition/pca.pkl`. These models are trained to recognize 2 classes in the <a href="http://vis-www.cs.umass.edu/lfw/">Labeled Faces in the Wild</a> dataset, using the Scikit-Learn example code <a href="https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html">here</a>.

Because the images in the Labeled Faces in the Wild dataset are 37 pixels by 50 pixels and greyscale, we resize all input images to this size and convert them to greyscale prior to input into the models. Note that the resize and greyscale operations are completed on the client side, so that less data would be sent to the server in the request message. This allows the input of large images (which would typically exceed the size of the message).

<img src="https://github.com/ArnoldYSYeung/grpc-image-service-prompt/blob/master/overview_images/client-server.png" alt="Facial Recognition pipeline" width=700 />

The PCA transformer extracts the principal components of the images (e.g., the principal facial components used for recognition which makes each class distinct) and convert them into features. The SVM classifier then uses these features to classify the image as 1 of the 2 classes.

I want to emphasize the <strong>limitations</strong> of this facial recognition method. The training data is comprised of low-quality photos of close-up headshots of each individual. As a consequence, images which are not close-up headshots may result in poor predictive performance. Furthermore, the predictive performance of this model is not state-of-the-art and is fairly low for modern standards, even for test images from the original dataset. It is expected that images not from the original dataset (with different original sizes and different cropping and position of the individuals' faces) would perform significantly worse. I selected the implementation of this model due to its relative low computation and not particularly for its accuracy.

The following accuracies were achieved for test images from the original dataset:

<img src = "https://github.com/ArnoldYSYeung/grpc-image-service-prompt/blob/master/overview_images/accuracy.PNG" alt="Facial recognition accuracy" width=300 />

<strong>NOTE</strong>: The code for training the PCA and SVM models is in Jupyter Notebook format in `./src/facial_recognition/facial_recognition_ETL.ipynb`. This code is not necessary for running the server.  You will need to install Matplotlib to run this code `python3 -m pip install matplotlib`.

### Unary RPC

Both microservices on this server use unary RPC to receive and send messages.

One of the key limitations of this server is its unary RPC. In unary RPC, a single request is sent from the client and a single response is returned by the server. This limits both the data amount available for sending a request and the operation speed and scalability of the service:

- Because only a single request (with a limited data size) is sent for each response, images of larger sizes, which require multiple messages, cannot be sent. This is avoided by scaling down the image in the image rotation service prior to sending to the server. 
- Because a client must receive a response after sending a request, the client must wait for the server to complete its service. While this may be trivial for instantaneous services, this may be cause significant wait times if the service is computationally intensive or if the service fails to return a response (e.g., due to a bug).


## Next Steps (Time Permitting)

Due to time constraints, the following were not implemented. I recommend such improvements:

### Streaming RPC
An alternative to the unary RPC would be a streaming RPC which would allow multiple chunks of messages to be sent as requests and responses. One of the limitations of the image rotation service is the inability to send over large images in a single message request. A bidirectional streaming RPC would allow the client to break down the image into several messages and send a stream of these messages to the server.  The server may then send back the rotated image in a stream of messages as well. This will allow the transfer of large images for the rotation service.

A streaming RPC is unnecessary for the current implementation of the facial recognition service. Because the facial recognition model operates with 30 pixels by 57 pixels greyscale images, all images, regardless of size, is downsampled prior to sending to the server. Therefore, an unary RPC would be sufficient for sending the entire image.

### Deep learning classification
Deep learning models, such as Convolutional Neural Networks (CNN), have been proven to outperform PCA and SVM models in facial recognition. The replacement of the PCA and SVM models with a trained CNN may provide both better classification performance and may be more suitable for larger images with greater variability. However, deep learning models are typically computationally expensive and require GPU processing power. Because I am unfamiliar with the build of the testing Linux machine, I opted for the simpler and safer option of PCA and SVM models, which uses Scikit-Learn which can run relatively efficiently on CPU.  Installing deep learning libraries and ensuring their compatiability with the machine is another major challenge, and might typically require individual configurations not foreseeable without the machine at hand.

Note that with a deep learning model for larger images, a client-streaming RPC, where the client may streaming chunks of messages representing a single image, may be necessary.

### Thread pooling
While the current implementation may be sufficient for a small team of engineers who are not running this service automated or concurrently, this server may be unable to handle high traffic from many requests sent at the same time. Using a large thread pool where a large number of threads is set and made available for concurrent requests would help mitigate this problem. Ideally, in the scenario where all the threads are occupied, additional requests would be queued. However, performance will then be dependent on the number of available processors because more processors would be necessary to handle higher number of threads and concurrent requests.

Because our implementation is in Python, the global interpreter lock (GIL) will limit the number of threads to the available processor cores, preventing a high number of threads from being executed at once. This is a major limitation to the deployment of such a server for high traffic applications.

### Image type support
The following server has been tested with `.jpg` and `.png` images. Further testing and additional support for images of other file types (e.g., `.webm`) may be necessary.


