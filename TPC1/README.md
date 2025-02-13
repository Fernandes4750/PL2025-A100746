# Relatório: Somador On/Off

**Data:** 13 de fevereiro de 2025  

## Autor  
**Nome:** Diogo Andrade Fernandes 

**Número:** A100746

![Foto do Autor](../imgs/foto-id.jpg)  

## Resumo  
- O objetivo deste trabalho foi desenvolver um programa em Python que soma números encontrados num texto de entrada.  
- O programa respeita comandos "On" e "Off" para ativar e desativar a soma, independentemente da capitalização.  
- Sempre que encontra o caractere "=", o programa imprime a soma acumulada até esse ponto.  
- No final do processamento, o valor total acumulado é também apresentado.  
- O código implementado segue um método simples de processamento sequencial sem o uso de expressões regulares.  

## Explicação da Resolução  

A implementação foi desenvolvida em **Python**, utilizando a biblioteca `sys` para ler o texto de entrada. O código segue uma abordagem sequencial baseada em manipulação de strings.

### **Estrutura e Lógica do Código**  

1. **Leitura do Texto de Entrada**  
   - O programa lê o texto completo a partir do `stdin` utilizando `sys.stdin.read()`.  
   - O texto é dividido em palavras usando `.split()`, separando os elementos por espaços.

2. **Variáveis Principais**  
   - `soma = 0` → Variável que armazena a soma dos números extraídos.  
   - `ativo = True` → Controla se os números devem ser somados ou ignorados.  

3. **Processamento do Texto**  
   - Percorre cada palavra do texto e verifica as seguintes condições:
     - Se a palavra for `"On"` (independentemente da capitalização), ativa a soma (`ativo = True`).
     - Se a palavra for `"Off"` (independentemente da capitalização), desativa a soma (`ativo = False`).
     - Se a palavra contiver `"="`, imprime a soma atual.
     - Caso contrário, tenta extrair **apenas os dígitos numéricos** da palavra.

4. **Extração de Números**  
   - Para evitar erros com palavras misturadas com letras e números (`"abc123"` ou `"90xyz"`), o código usa:
     ```python
     num = "".join(filter(str.isdigit, palavra))
     ```
     - O método `filter(str.isdigit, palavra)` percorre cada caractere e mantém **apenas os dígitos**.
     - Se a palavra resultante for um número válido (`num.isdigit()`), converte-o para inteiro (`int(num)`) e soma-o **se a variável `ativo` for `True`**.

5. **Impressão da Soma**  
   - Sempre que encontra `"="`, o programa imprime a soma acumulada até aquele ponto:
     ```python
     if "=" in palavra:
         print(soma)
     ```
   - No final do processamento, imprime o valor total da soma.

## Lista de Resultados  
- [Código-fonte do programa](SomadorOnOff.py)  
- [Ficheiro de entrada](input.txt)  
- [Descrição do problema](tpc1.pdf)  
