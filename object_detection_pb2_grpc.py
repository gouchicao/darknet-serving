# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import object_detection_pb2 as object__detection__pb2


class ObjectDetectionStub(object):
  """darknet yolov3 object detection
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.detect = channel.stream_unary(
        '/ObjectDetection/detect',
        request_serializer=object__detection__pb2.UploadImageRequest.SerializeToString,
        response_deserializer=object__detection__pb2.DetectResponse.FromString,
        )


class ObjectDetectionServicer(object):
  """darknet yolov3 object detection
  """

  def detect(self, request_iterator, context):
    """客户端到服务器端的流式RPC
    对图像的数据进行对象检测
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ObjectDetectionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'detect': grpc.stream_unary_rpc_method_handler(
          servicer.detect,
          request_deserializer=object__detection__pb2.UploadImageRequest.FromString,
          response_serializer=object__detection__pb2.DetectResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ObjectDetection', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))