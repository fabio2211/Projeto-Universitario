def contar_vogais(texto) : 
 contador = 0
 vogais = 'aeiouAEIOU'
 for letra in texto:
    if letra in vogais :
        contador +=1
 return contador