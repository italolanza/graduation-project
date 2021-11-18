# cONNXr

É um runtime para [[ONNX]] escrito puramente em C99 sem qualquer dependência externa que faz a inferência em modelos no formato `.onnx`.


<br>

## Basic workflow
Executa os modelos no formato `.onnx` utilizando como entrada protobufs (arquivos `.pb`).


```bash
build/connxr <model.onnx> <input.pb>
```
