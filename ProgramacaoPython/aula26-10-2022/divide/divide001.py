"""
Programa divide
Requisito: Crie um programa que leia dois números inteiros
do teclado, calcule a razão entre o primeiro e o segundo e
resultado. 
Autor: Rodrigo Damasceno Soares
Data: 26/10/2022
Versão 0.0.1
"""

# Entrada

print ("Este programa calcula a razão entre dois números dados pelo usuário")

numerador = int (input("\nDigite o numerador: "))
denominador = int (input("\nDigite o denominador: "))

# Processamento

razao = numerador / denominador

# Saída

print (f"A razão entre o número {numerador} e o número {denominador} é: {razao}")
