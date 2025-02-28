# **Relatório: Conversor de Markdown para HTML**

**Data:** 28 de fevereiro de 2025  

## **Autor**  
**Nome:** Diogo Andrade Fernandes  
**Número:** A100746  

![Foto do Autor](../imgs/foto-id.jpg)  

---

## **Resumo**  
O objetivo deste trabalho foi desenvolver um **conversor de Markdown para HTML** utilizando **Python**, respeitando as regras da **Basic Syntax** da Markdown Cheat Sheet. O programa deve processar os seguintes elementos:

- **Cabeçalhos:** `#`, `##` e `###` convertidos em `<h1>`, `<h2>`, `<h3>`.
- **Negrito:** `**texto**` convertido em `<b>texto</b>`.
- **Itálico:** `*texto*` convertido em `<i>texto</i>`.
- **Listas numeradas:**
  ```markdown
  1. Item 1
  2. Item 2
  3. Item 3
  ```

  convertidas em:
  ```html
  <ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ol>
  ```
- **Links:** `[texto](URL)` convertido em `<a href="URL">texto</a>`.
- **Imagens:** `![texto alternativo](URL)` convertido em `<img src="URL" alt="texto alternativo"/>`.

O programa processa um ficheiro de entrada Markdown (`input.md`) e gera um ficheiro HTML de saída (`output.html`).

---

## **Explicação da Resolução**

### **1. Leitura e Processamento do Ficheiro**
O programa lê um ficheiro Markdown (`input.md`) e aplica uma série de funções para identificar e converter os elementos Markdown para HTML. 

### **2. Conversão dos Elementos Markdown para HTML**
Os cabeçalhos são convertidos de acordo com a hierarquia `#`, `##` e `###`. O negrito e itálico são identificados e transformados em `<b>` e `<i>`, respetivamente. As imagens e links são extraídos e formatados em HTML. Listas numeradas são agrupadas corretamente dentro de `<ol>` e `<li>`.

### **3. Escrita do Ficheiro de Saída**
Após a conversão, o conteúdo HTML gerado é gravado num ficheiro (`output.html`). Se ocorrer um erro ao abrir ou gravar o ficheiro, o programa exibe uma mensagem de erro apropriada.

---

## **Lista de Resultados**
- [Ficheiro de entrada](input.md)  
- [Ficheiro de saída](output.html)  
- [Descrição do problema](tpc3.pdf)  

---

## **Conclusão**
O programa desenvolvido permite converter corretamente os elementos básicos do Markdown em HTML, seguindo as regras da "Basic Syntax". Ele processa o ficheiro de entrada, converte os elementos e gera um ficheiro HTML corretamente formatado.  

Este conversor pode ser expandido para suportar mais elementos do Markdown, como listas não ordenadas, blocos de código e tabelas.  
