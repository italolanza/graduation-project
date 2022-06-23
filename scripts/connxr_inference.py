#!/usr/bin/env python3

from config import models_path, frameworks_path
from os import system
from pathlib import Path

connxr_runtime = Path(frameworks_path['connxr']).joinpath('build','connxr')
onnx_model = models_path['connxr']
input_data = '/home/italolanza/workspace/TG/dataset/x_test.pb'
# output_path = '/home/italolanza/workspace/TG/output/connxr_dumpfile.txt'

cmd = f'{connxr_runtime} {onnx_model} {input_data} --dump-file'

#run the command
system(cmd)