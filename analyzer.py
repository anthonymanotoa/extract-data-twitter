# Palabras a excluir
exclude_words = ['el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'al', 'del', 'lo', 'le', 'y', 'e', 'o', 'u', 'de', 'a', 'en', 'que', 'es', 'por', 'para', 'con', 'se', 'su', 'les', 'me', 'q', 'te', 'pero', 'mi', 'ya', 'cuando', 'como', 'estoy', 'voy', 'porque', 'he', 'son', 'solo', 'tengo', 'muy']


# Generar un diccionario con todas las palabras
top_words = {}
tweets_topic = open('./onepiece.txt', encoding='utf-8')
for line in tweets_topic:
    words = line.strip().lower().split()
    for word in words:
        if word not in exclude_words:
            top_words[word] = top_words.get(word, 0) + 1


# Ordenar desde las más usadas hasta las menos usadas
most_used_words = sorted(top_words, key=top_words.get, reverse=True)


# Cuentas más relevantes
count_u = 0
for word in most_used_words:
    if count_u <10 and word.startswith('@'):
        print(top_words[word], word)
        count_u += 1

print('*'*40)


# Palabras más usadas
count = 0
for word in most_used_words:
    if count < 30:
        print(top_words[word], word)
        count += 1