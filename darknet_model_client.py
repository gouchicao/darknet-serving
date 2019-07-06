from __future__ import print_function

import random
import logging
import argparse

import grpc

import object_detection_pb2
import object_detection_pb2_grpc


BLOCK_SIZE = 40000


class ImageDataBlockRequestIterable(object):
    def __init__(self, img_data):
        self.data = img_data
        self.pos = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        data_block = self.data[self.pos:self.pos+BLOCK_SIZE]
        if data_block:
            request = object_detection_pb2.UploadImageRequest(
                data_block = data_block
            )
            self.pos += BLOCK_SIZE
            return request
        else:
            raise StopIteration


class gRPCClient():
    def __init__(self, server_address):
        logging.basicConfig()

        channel = grpc.insecure_channel(server_address)
        self.stub = object_detection_pb2_grpc.ObjectDetectionStub(channel)

    def detect(self, img_data):
        if img_data:
            data_block_iterable = ImageDataBlockRequestIterable(img_data)

            try:
                response = self.stub.detect(data_block_iterable)
                return response
            except grpc.RpcError as err:
                print(err.details()) #pylint: disable=no-member
                #print('{}, {}'.format(err.code().name, err.code().value())) #pylint: disable=no-member
        else:
            print('image data is none.')


def read_image(filename):
    img_data = None
    with open(filename, 'rb') as f:
        img_data = f.read()
    return img_data


# python darknet_model_client.py -a 127.0.0.1:7713 -f ../darknet/model-zoo/platen-switch/test/IMG_9256.JPG
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--server_address', type=str, help='server address 127.0.0.1:7713', default='[::]:7713')
    parser.add_argument('-f', '--image_file', type=str, help='image file path.')
    
    args = parser.parse_args()

    if args.server_address and args.image_file:
        img_data = read_image(args.image_file)
        
        client = gRPCClient(args.server_address)
        response = client.detect(img_data)
        print(response)
    else:
        print("argument isn't none.")

