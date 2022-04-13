# Does not work

import torch
import torch.onnx
import onnx
import onnxruntime as rt


input_file_path = '/home/italolanza/workspace/TG/graduation-project/models/sequential.onnx'
output_filename = "/home/italolanza/workspace/TG/graduation-project/models/model_exported_from_pytorch.onnx"

print("Loading {}".format(input_file_path))

onnx_model = onnx.load(input_file_path)
onnx.checker.check_model(onnx_model)

providers = ['CPUExecutionProvider']
sess_options = rt.SessionOptions()
sess_options.enable_profiling = True

session = rt.InferenceSession(input_file_path, providers=providers, sess_options=sess_options)
input_name = [session.get_inputs()[0].name]
output_name = [session.get_outputs()[0].name]

# in order to export the model, torch needs to run one forward inference
# to compute the model graph.  We can do this with a random input.
x = torch.randn(1, 40 ,requires_grad=True)

# print(x)
# Export the model
print("Exporting {}".format(output_filename))
torch_out = torch.onnx.export(onnx_model,         # model being run
                              x,                   # model input 
                              output_filename,     # where to save the model 
                              input_names=input_name,
                              output_names=output_name,
                              verbose=True,
                              export_params=True)  # store the trained weights