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

<br>

## Deploying

### Fixing the Dockerfile

```
Passos:
	-> adicionar o tar do llvm-8 ao docker file
		-> mover os diretorios de dentro da pasta criada
	-> mudar/tirar a versao dos compiladores do comando cmake <...>
	-> instalar o flask8
```

### Converting the ONNX model to ELL

```shell
python <ELL-root>/tools/importers/ONNX/onnx_import.py model.onnx
```

### Deploying the EEL model

Deploying an ELL model requires two steps. **First**, you’ll run the wrap tool, which both compiles the `featurizer.ell` and `classifier.ell` models into machine code and generates a CMake project to build a Python wrapper for it. **Second**, you’ll call CMake to build the Python library.

```shell
python <ELL-root>/tools/wrap/wrap.py --model_file featurizer.ell --target host --outdir compiled_featurizer --module_name mfcc

python <ELL-root>/tools/wrap/wrap.py --model_file classifier.ell --target host --outdir compiled_classifier --module_name model
```