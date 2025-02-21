# **Relatório: Análise de um Dataset de Obras Musicais**

**Data:** 21 de fevereiro de 2025  

## **Autor**  
**Nome:** Diogo Andrade Fernandes  
**Número:** A100746  

![Foto do Autor](../imgs/foto-id.jpg)  

---

## **Resumo**  
O objetivo deste trabalho foi desenvolver um programa em **Python** para processar um **dataset de obras musicais** contido num ficheiro CSV. O programa **não pode usar o módulo `csv`** e deve processar manualmente os dados para gerar os seguintes resultados:

- **Lista ordenada alfabeticamente dos compositores musicais.**  
- **Distribuição das obras por período, indicando quantas existem em cada um.**  
- **Dicionário onde cada período está associado a uma lista alfabética das obras desse período.**  

O código foi implementado utilizando **expressões regulares** para extrair os dados e **dicionários** para organizar as informações.

---

## **Explicação da Resolução**

### **1. Leitura do Dataset**
- O ficheiro `obras.csv` contém um conjunto de obras musicais organizadas em colunas separadas por ponto e vírgula (`;`).
- Como o uso do módulo `csv` é proibido, a leitura e o processamento do ficheiro foram feitos manualmente, **linha por linha**.
- Para ignorar a primeira linha (cabeçalho), o código usa um **sinalizador (`proxima_linha`)** para começar a leitura real apenas na segunda linha.

```python
with open(file_path, 'r', encoding='utf-8') as obras:
    proxima_linha = False
    buffer = ""
    for linha in obras:
        if not proxima_linha:
            proxima_linha = True
            continue
```

---

### **2. Extração dos Dados**
- A extração dos dados do CSV foi feita com uma **expressão regular**, garantindo que cada campo seja corretamente capturado, incluindo aqueles com aspas (para evitar problemas com valores que contêm ponto e vírgula).

```python
pattern = re.compile(r'([^;]+);("(?:[^"]*(?:"[^"]*)*)"|[^;]+);([^;]+);([^;]+);([^;]+);([^;]*)\n?')
```

- Os campos extraídos são:
  - **Título da obra**  
  - **Período musical**  
  - **Compositor**  

- Após a correspondência com a expressão regular, os valores são armazenados em **dicionários** para facilitar a organização.

```python
match = re.match(pattern, buffer)
if match:
    nome = match.group(1)  # Título da obra
    periodo = match.group(4)  # Período
    compositor = match.group(5)  # Compositor
```

---

### **3. Organização dos Dados**
Para estruturar os resultados, foram utilizados **três estruturas de dados principais**:

1. **Lista de compositores ordenada**  
   - Utiliza um **conjunto (`set()`)** para evitar duplicação de nomes e depois ordena alfabeticamente.

```python
compositores = set()
compositores.add(compositor)
```

2. **Distribuição das obras por período**  
   - Utiliza um **dicionário (`defaultdict(int)`)** onde a chave é o período e o valor é o número de obras.

```python
distribuicao_periodos = defaultdict(int)
distribuicao_periodos[periodo] += 1
```

3. **Lista de obras organizadas por período**  
   - Utiliza um **dicionário (`defaultdict(list)`)** onde a chave é o período e o valor é uma lista ordenada de títulos das obras.

```python
obras_por_periodo = defaultdict(list)
obras_por_periodo[periodo].append(nome)
```

---

### **4. Ordenação e Impressão dos Resultados**
- **Ordenar compositores alfabeticamente**
```python
compositores = sorted(compositores)
```

- **Ordenar títulos das obras dentro de cada período**
```python
for periodo in obras_por_periodo:
    obras_por_periodo[periodo].sort()
```

- **Impressão da Lista de Compositores**
```python
print("\n### Lista de Compositores (Ordenada) ###")
for compositor in compositores:
    print(compositor)
```

- **Impressão da Distribuição das Obras por Período**
```python
print("\n### Distribuição de Obras por Período ###")
for periodo, quantidade in distribuicao_periodos.items():
    print(f"{periodo}: {quantidade} obras")
```

- **Impressão das Obras Organizadas por Período**
```python
print("\n### Obras Organizadas por Período ###")
for periodo, obras in obras_por_periodo.items():
    print(f"\n{periodo}:")
    for obra in obras:
        print(f"  - {obra}")
```

---

## **Lista de Resultados**
- [Código-fonte do programa](obras.py)  
- [Ficheiro de entrada](obras.csv)  
- [Descrição do problema](tpc2.pdf)  

---

## **Conclusão**
O programa desenvolvido cumpre todos os requisitos do **TPC2** sem utilizar o módulo `csv`, respeitando as restrições impostas. A estrutura escolhida permitiu **uma organização eficiente dos dados**, garantindo que os compositores e as obras sejam corretamente ordenados e classificados por período. 