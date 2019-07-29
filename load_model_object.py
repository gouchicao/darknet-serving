import darknet
import config


def get():
    if get.model:
        return get.model
    else:
        get.model['net'] = darknet.load_net(bytes(config.model_files['net_cfg'], "utf-8"), 
                                            bytes(config.model_files['net_weight'], "utf-8"), 
                                            0)
        get.model['meta'] = darknet.load_meta(bytes(config.model_files['metadata'], "utf-8"))


get.model = {}
