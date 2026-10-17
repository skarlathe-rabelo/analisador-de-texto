# Analisador de Texto

Programa em Python que analisa um texto colado pelo usuário e mostra estatísticas simples sobre ele.

## O que ele faz
- Conta caracteres (com e sem espaços)
- Conta palavras
- Conta frases
- Mostra as 5 palavras mais usadas

## Como usar
1. Tenha o Python 3 instalado
2. Baixe o arquivo `analisador.py`
3. Execute no terminal: `python analisador.py`
4. Cole um texto quando o programa pedir e aperte Enter

## Limitações conhecidas
- Abreviações com ponto (como "Mr." e "Sr.") são contadas como fim de frase
- Reticências (...) contam como mais de uma frase

## O que aprendi
Pratiquei entrada de dados com `input`, listas, laços (`for`), condicionais (`if`) e dicionários em Python. Também tratei o texto (minúsculas e remoção de pontuação) para contar palavras corretamente.

## Próximos passos
- Calcular o tempo estimado de leitura
- Organizar o código em funções
- Ignorar palavras muito curtas (como "o", "de")
