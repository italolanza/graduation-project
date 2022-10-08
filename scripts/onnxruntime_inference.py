#!/usr/bin/env python3

import onnxruntime as rt
import onnx
import numpy as np
from config import models_path
from data import x_data, y_data
from memory_profiler import profile

# Load a TensorProto
# new_tensor = onnx.TensorProto()
# with open(models_path['onnx'], 'rb') as f:
    # new_tensor.ParseFromString(f.read())

# load and the onnx model
onnx_model = onnx.load(models_path['onnx'])
onnx.checker.check_model(onnx_model)

# set the provider and session options
providers = ['CPUExecutionProvider']
sess_options = rt.SessionOptions()
sess_options.enable_profiling = True

# creates the inference session
session = rt.InferenceSession(models_path['onnx'], providers=providers, sess_options=sess_options)
input_name = [session.get_inputs()[0].name]
output_names = [session.get_outputs()[0].name]

# @profile
def run_inference():
    # start = timer()
    # run the predictions
    onnx_pred = session.run(output_names, {"input":np.float32(x_data)})
    # session.end_profiling()
    # end = timer()
    # print(f"{end - start} seconds to execute the inference !") # Time in seconds, e.g. 5.38091952400282
    return onnx_pred



if __name__ == '__main__':
    onnx_pred = run_inference()
    session.end_profiling()
    
    # results
    # print('ONNX Output:', onnx_pred[0])

    # make sure ONNX and keras have the same results
    # np.testing.assert_allclose(predictions, onnx_pred[0], rtol=1e-5)
    # print('Expected Output:', y_data)