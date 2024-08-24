# Curso Intermediário de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício de Range

minha_lista =[7,9,13,15,18,23,29,32,33,39]
for iter_var in range(len(minha_lista)):
    minha_lista.append(minha_lista[iter_var]+2)
    print(minha_lista)