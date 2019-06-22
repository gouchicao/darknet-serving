from __future__ import print_function

import random
import logging

import grpc

import object_detection_pb2
import object_detection_pb2_grpc


BLOCK_SIZE = 40000


class ImageDataBlockRequestIterable(object):
    def __init__(self, img_path):
        self.img_path = img_path
        
        with open(img_path, 'rb') as f:
            self.data = f.read()
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
    def __init__(self):
        channel = grpc.insecure_channel('127.0.0.1:7713')
        self.stub = object_detection_pb2_grpc.ObjectDetectionStub(channel)

    def detect(self, img_path):
        data_block_iterable = ImageDataBlockRequestIterable(img_path)

        try:
            response = self.stub.detect(data_block_iterable)
            print('Photo uploaded.')
            return response
        except grpc.RpcError as err:
            print(err.details()) #pylint: disable=no-member
            #print('{}, {}'.format(err.code().name, err.code().value())) #pylint: disable=no-member
        

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    #with grpc.insecure_channel('localhost:50051') as channel:
    #    stub = analyze_pb2_grpc.AnalyzeStub(channel)
    #    print("-------------- detect_image --------------")
    #    stub.detect_image(analyze_pb2.DetectRequest())
    client = gRPCClient()
    response = client.detect("test-images/IMG_9256.JPG")
    print(response)


if __name__ == '__main__':
    logging.basicConfig()
    run()

