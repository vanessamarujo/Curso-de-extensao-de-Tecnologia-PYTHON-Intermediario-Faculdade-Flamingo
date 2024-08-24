# Curso Intermediário de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício de Laço for

# Código para encontrar a soma dos quadrados de cada elemento da lista usando o loop for  

# criando a lista de números
numeros=[3,5,23,6,5,1,2,9,8]
# inicializando uma variável que armazenará a soma
soma=0
# usando o loop for para iterar sobre a lista  
for num in numeros:
    soma = soma + num**2
    print ("A soma dos números é: ",soma)

