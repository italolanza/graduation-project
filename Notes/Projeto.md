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
		- `4` inner and outer bearing faults (rolamento inferior.
- O nível de criticidade;
	- `Low`
	-  `Medium`
	-  `High`

## Versão Inicial 

- Versão inicial: 
	- Integer/Probabilidade
		- `0` normal function
		- `1` imbalance fault
		- `2` horizontal misalignment fault
		- `3` vertical misalignment fault 
- O nível de criticidade (float ?);
	- `0.0 -> Normal`
	- `1.0 -> Low`
	- `2.0 -> Medium`
	- `3.0 -> High`


	
### Definição de Critricidade

- **Normal** -> Always `low`
- **Imbalance**
	- **`Low`** -> 6g, 10g
	- **`Medium`** -> 15g, 20g, 25g
	- **`High`** -> 30g, 35g
- **Horizontal Misalignment**
	- **`Low`** -> 0.5mm
	- **`Medium`** -> 1.0mm, 1.5mm
	- **`High`** -> 2.0mm
-  **Vertical Misalignment**
  	- **`Low`** -> 0.51mm, 0.63mm
	- **`Medium`** -> 1.27mm, 1.40mm
	- **`High`** -> 1.78mm, 1.90mm