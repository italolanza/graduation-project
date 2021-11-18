# Estrutura básica da rede

**Entrada:**
- Sinal Bruto ?
- FFT do Sinal ?

**Saída da Rede:**
- Qual o problema (tipo de desalinhamento);
	- Probabilidade
		- `0` normal function
		- `1` imbalance fault
		- `2` horizontal misalignment fault
		- `3` vertical misalignment fault 
		- `4` inner and outer bearing faults.
- O nível de criticidade;