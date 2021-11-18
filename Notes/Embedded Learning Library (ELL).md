# Embedded Learning Library (ELL)
---

É uma biblioteca que acompanha um série de ferramentas escritas em C++ e Python o qual é capaz de compular redes neurais treinadas, utilizando o padrão [[ONNX]], para código de máquina utilizando da estrutura da [LLVM](https://llvm.org/).


## Implementações

### Biblioteca `data`

Implementa uma interface (e uma estrutura de dados) de um `DataVector`, que consiste em um vetor especializado em armazenar dados. O *DataVector* e representado como uma sequencia de *doubles*, porém internamente ele pode ser armazenado na memória de diversas formas, tais como:

- `std::vector<double>`
- `std::vector<float>`
- `std::vector<short>`
- `std::vector<char>`

> Verificar [documentação](https://github.com/microsoft/ELL/blob/master/libraries/data/doc/README.md) para mais informações das implementações do *DataVector* e também funções de suporte.

Além das implementações e funções de apoio, a biblioteca também implementa diversas operações lineares entre um vetor de data (*DataVector*) e um vetor `math::Vector`.


### Biblioteca `math`

### Bibliotecas `model` e `nodes`


-   [Design overview of `data` library](https://github.com/microsoft/ELL/blob/master/libraries/data/doc/README.md)
-   [Design overview of `math` library](https://github.com/microsoft/ELL/blob/master/libraries/math/doc/README.md)
-   [Design overview of `model` and `nodes` libraries](https://github.com/microsoft/ELL/blob/master/libraries/model/doc/README.md)