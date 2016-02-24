from utils import config_pb2

config = config_pb2.Config()

config.enable_core_modeling = True
config.enable_power_modeling = True

with open("config.bin", "wb") as f:
    f.write(config.SerializeToString())
