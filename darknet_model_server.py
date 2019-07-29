import argparse
import logging

import object_detection_grpc as grpc
import object_detection_rest as rest


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', type=str, 
                        default='grpc', choices=['grpc', 'rest'], 
                        help='Interface service grpc or rest.')

    args = parser.parse_args()

    logging.basicConfig()

    if args.mode == 'grpc':
        grpc.serve()
    else:
        rest.serve()
