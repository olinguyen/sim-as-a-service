import os
import sys
GRAPHITE_HOME = os.environ.get('GRAPHITE_HOME')
DEFAULT_CONFIG = "/root/sim-as-a-service/utils/default_config.cfg"

CHOLESKY = "cholesky_bench_test"
BARNES   = "barnes_bench_test"
PINGPONG = "ping_pong_app_test"
FFT      = "fft_bench_test"
RUNNING_SIM_FLAG = GRAPHITE_HOME + "tools/running_sim"

SIM_OUTPUT_PATH = GRAPHITE_HOME + 'results/latest'

CONFIG_PATH = "/root/sim-as-a-service/configs/"
SPAWN_APP = "/root/sim-as-a-service/utils/spawn.py"
