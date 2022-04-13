# TensorFlow
TensorFlow is a software library extensively used in machine learning. TensorFlow uses a high-level API called [Keras](https://www.tensorflow.org/guide/keras) that provides a powerful, intuitive framework for building and training deep learning models.

<br>

## Tensor
São arrays/vetores de n-dimensões. O **`shape`** de um Tensor define o tamanho (numero de elementos) de cada uma de suas dimesões e o **`rank`** define a quantidade de dimensões do mesmo.

<br>

## Notas
+ No TensorFlow, o `shape` e contabilizado de fora para dentro. Isto considera-se primeiro o tamanho da dimensao mais externas e depois o tamanho das dimensoes mais internas.
+ Podemos pensar em operações em Tensores em termos de grafos (direcionais, hierarquicos e aciclicos). Um nó pode ser um Tensor (dados) ou uma operação aplicada a outros nós (Tensores) com possíveis entradas e que pode fornecer saídas.
+ No TensorFlow, `Graphs` são conjuntos de *nodes* (nós) conectados. Essas conexões são chamadas de `edges` (arestas).
+ **`Variables`** conseguem amarzenar valor de pesos e *bias* durante sessões (*sessions*) porém precisam ser inicializadas antes de serem usadas em uma sessão;
+ **`Placeholders`** são inicialmente vazios e depos são preenchidos com os valores de treinamento.
  + É necessário declarar o tipo de dado que o `Placeholder` irá armazenar préviamente e opcionalmente o *shape*;


<br>

# TensorFlow Lite

## Inferencia
Conceitos importantes

A inferência do TensorFlow Lite normalmente segue as seguintes etapas:

1. **Carregando um modelo:** Você deve carregar o .tflite modelo na memória, que contém gráfico de execução do modelo.
2. **Transformando dados:** Os dados de entrada brutos para o modelo geralmente não correspondem ao formato de dados de entrada esperado pelo modelo. Por exemplo, você pode precisar redimensionar uma imagem ou alterar o formato da imagem para ser compatível com o modelo.
4. **Inferência de execução:** Esta etapa envolve o uso da API TensorFlow Lite para executar o modelo. Envolve algumas etapas, como construir o interpretador e alocar tensores, conforme descrito nas seções a seguir.
5. **Produção de interpretação:** Ao receber os resultados da inferência do modelo, você deve interpretar os tensores de uma forma significativa que seja útil em sua aplicação. Por exemplo, um modelo pode retornar apenas uma lista de probabilidades. Cabe a você mapear as probabilidades para categorias relevantes e apresentá-las ao seu usuário final.

### Executando um modelo

Executar um modelo TensorFlow Lite envolve algumas etapas simples:

1. Carregue o modelo na memória.
2. Construir um Interpreter com base em um modelo existente.
3. Defina os valores do tensor de entrada. (Opcionalmente, redimensione os tensores de entrada se os tamanhos predefinidos não forem desejados.)
4. Invoque inferência.
5. Leia os valores do tensor de saída.