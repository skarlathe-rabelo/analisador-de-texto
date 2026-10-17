texto = input("Cole seu texto: ")

# Etapa 1: caracteres e palavras
caracteres = len(texto)
caracteres_sem_espacos = len(texto.replace(" ", ""))
palavras = texto.split()
quantidade_palavras = len(palavras)

# Etapa 2: frases
frases = 0
for caractere in texto:
    if caractere in ".!?":
        frases = frases + 1

print("Caracteres:", caracteres)
print("Caracteres sem espaços:", caracteres_sem_espacos)
print("Palavras:", quantidade_palavras)
print("Frases:", frases)

# Etapa 3: palavras mais usadas
texto_limpo = texto.lower()
for sinal in ".,!?;:\"()":
    texto_limpo = texto_limpo.replace(sinal, "")
lista_palavras = texto_limpo.split()

contagem = {}
for palavra in lista_palavras:
    if palavra in contagem:
        contagem[palavra] = contagem[palavra] + 1
    else:
        contagem[palavra] = 1

mais_usadas = sorted(contagem.items(), key=lambda item: item[1], reverse=True)

print("Palavras mais usadas:")
for palavra, vezes in mais_usadas[:5]:
    print(palavra, "-", vezes, "vez(es)")
