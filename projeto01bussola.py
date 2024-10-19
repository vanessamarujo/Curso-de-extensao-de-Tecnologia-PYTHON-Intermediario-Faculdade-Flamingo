
#Projeto01 -Python bussola

import random
#definindo uma funcao em Python

def bussola():
    #criar uma lista com os pontos cardeais em inglês
    pontos_cardeais=["Norte","Nordeste","Leste","Sudeste","Sul","Sudoeste","Oeste","Noroeste"] 
    
    #Gerando um  numero aleatorio de 0 a 7 para representar os pontos cardeais
    direcao=random.randint(0,7)
    print("Você esta virado para o ponto cardeal",pontos_cardeais[direcao])
    
bussola()