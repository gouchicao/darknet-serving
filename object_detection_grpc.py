from concurrent import futures
import time
import math
import logging
import tempfile

import grpc

import object_detection_pb2
import object_detection_pb2_grpc

import darknet
import config
import load_model_object


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ObjectDetectionServicer(object_detection_pb2_grpc.ObjectDetectionServicer):
    """darknet yolov3 object detection
    """

    def detect(self, request_iterator, context):
        """客户端到服务器端的流式RPC
        对图像的数据进行对象检测
        """
        print('detect')
        data_blocks = []
        for request in request_iterator:
            data_blocks.append(request.data_block)
            if len(data_blocks) > 100:
                return error_handler.throw_exception(
                    grpc_context=context,
                    code=grpc.StatusCode.FAILED_PRECONDITION,
                    details='FAILED_PRECONDITION: Image is oversized.'
                )

        detect_result = None
        img_data = b''.join(data_blocks)
        with tempfile.NamedTemporaryFile() as f:
            f.write(img_data)
            detect_result = darknet.detect(load_model_object.get.model['net'], 
                                           load_model_object.get.model['meta'], 
                                           f.name.encode("utf-8"))

        objects = []
        for item in detect_result:
            rect = item['rectangle']
            obj = object_detection_pb2.Object(name=item['object'],
                confidence=item['confidence'],
                rectangle=object_detection_pb2.Rectangle(x=rect['x'], y=rect['y'], w=rect['w'], h=rect['h'])
            )
            objects.append(obj)
        return object_detection_pb2.DetectResponse(object=objects)


def serve():
    load_model_object.get()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=config.server_max_workers))
    object_detection_pb2_grpc.add_ObjectDetectionServicer_to_server(
        ObjectDetectionServicer(), server)
    server_address = '{}:{}'.format(config.server_address, config.server_port)
    server.add_insecure_port(server_address)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

