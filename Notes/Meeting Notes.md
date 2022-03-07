# Notas Reuniões com Suyama

## 2021

### 17 de Agosto de 2021

- Plaforma de testes: **Raspberry Pi 3**
    + Implementar 
- Verificar no trabalho se vale á pena a utilização desse padrão ONNX
    + Implementar uma rede no formato ONNX e depois testar no Raspberry cada uma das bibliotecas
- Mostrar o fluxo de como funciona desde o treinamento até o deploy no hardware

<br>

### 14 de Setembro

- Pensar em algum tipo de aplicação em que possa ser utilizado o TG


<br>

### 21 de Setembro

- Criar uma uma rede neural simples e treina-la para reconhecer algum padrão baseado em um sensor lido através dos pinos do Raspberry;



<br>

### 05 de Outubro

-  Objetivo do meu projeto não e propor uma soluçao de ML para um problema novo, mas mostrar como implementar um rede utilizando as bibliotecas de ML para dispositivos embarcados


- Solução base no computador
	- Testar diferentes de redes neurais
		- Depois de decidir um modelo, implementar no raspberry a solução e testa-la colocando valores de entrada

<br>

## 2022

### 16 de Fevereiro de 2022

- Ao invés de usar o TensorFlow talvez usar o Keras;

1. Preparar Raspberry para rodar o código Python
2. Implementar Rede Neural (TensorFlow)
3. Exportar estrutura da rede no formato ONNX
4. Implementar usando framework usado na revisão (ao menos 2)
5. Avaliar:
   1. Tempo de execução
   2. Consumo de recursos

Texto: Mudar de Dispositivos Embarcadas para Sistemas Embarcadas
    Falar um pouco a respeito e quais os desafios;
    Falar dos possíveis usos de redes neurais em sistemas embarcados
        Citar exemplos?

    Falar sobre detecção de falhas em máquinas rotativas
    -> Verificar realtorio no overleaf que o Suayama editou


**Entrada:**
- Sinal Bruto ?
- FFT do Sinal ?

**Saída da Rede:**
- Qual o problema (tipo de desalinhamento);
- O nível de criticidade;


8/04 Indicação da banca
18/04 ~ 29/04 Apresentação
06/05 Entrega versão final

[28/02] 0 - Rodar código na CPU
[28/02] 1 - Rodar código Python na Raspberry
[28/02] 2 - Implementar Rede Neural (Tensorflow)

[11/03] 3 - Exportar estrutura da rede no formato ONNX (ou outro)
[11/03] 4 - Implementar usando framework encontrado na revisão (ao menos 2)
[25/03] 5 - Testes de a) Tempo de execução, b) Consumo de recursos
