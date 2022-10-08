#!/usr/bin/env python3

from config import models_path, frameworks_path
from os import system
from pathlib import Path
from memory_profiler import profile
from timeit import default_timer as timer

connxr_runtime = Path(frameworks_path['connxr']).joinpath('build','connxr')
onnx_model = models_path['connxr']
# input_data = '/home/italolanza/workspace/TG/dataset/x_test.pb' # desktop
input_data = '/home/italolanza/Workspace/TG/dataset/x_test.pb' # laptop
# output_path = '/home/italolanza/workspace/TG/output/connxr_dumpfile.txt'

# cmd = f'{connxr_runtime} {onnx_model} {input_data} --dump-file'
cmd = f'{connxr_runtime} {onnx_model} {input_data}'

#run the command
@profile
def run_inference():
    # start = timer()
    # run the predictions
    system(cmd)
    # session.end_profiling()
    # end = timer()
    # print(f"{end - start} seconds to execute the inference !") # Time in seconds, e.g. 5.38091952400282


run_inference()
