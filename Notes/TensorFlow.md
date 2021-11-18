# TensorFlow
TensorFlow is a software library extensively used in machine learning. TensorFlow uses a high-level API called [Keras](https://www.tensorflow.org/guide/keras) that provides a powerful, intuitive framework for building and training deep learning models.

<br>

## Tensor
São arrays/vetores de n-dimensões. O **`shape`** de um Tensor define o tamanho (numero de elementos) de cada uma de suas dimesões e o **`rank`** define a quantidade de dimensões do mesmo.

<br>

## Notas
+ No TensorFlow, o `shape` e contabilizado de fora para dentro. Isto considera-se primeiro o tamanho da dimensao mais externas e depois o tamanho das dimensoes mais internas.
+ Podemos pensar em operações em Tensores em termos de grafos (direcionais, hierarquicos e aciclicos). Um nó pode ser um Tensor (dados) ou uma operação aplicada a outros nós (Tensores).